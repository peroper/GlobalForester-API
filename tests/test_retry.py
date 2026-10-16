import io

import pytest
from fake_session import FakeResponse, FakeSession

import utils

TOO_MANY = {'status': 429, 'detail': 'Too many Forestand calls are running at once.',
            'code': 'tooManyConcurrentRequests'}


def api(*responses, **kwargs):
    slept = []
    client = utils.Api(
        host='https://api.test',
        token='t',
        session=FakeSession(responses),
        sleep=slept.append,
        **kwargs)
    return client, slept


def test_a_429_is_waited_out_for_the_seconds_in_retry_after_and_then_asked_again():
    client, slept = api(
        FakeResponse(status_code=429, body=TOO_MANY, headers={'Retry-After': '7'}),
        FakeResponse(body={'importId': 'imp-1', 'managedAreaIds': ['ma-1']}))

    result = client.post_xml('/v4/teams/team-1/forestand', lambda: b'<plan/>')

    assert slept == [7]
    assert result['importId'] == 'imp-1'


def test_a_429_that_keeps_coming_is_given_up_on_and_still_says_how_long_to_wait():
    client, slept = api(
        *[FakeResponse(status_code=429, body=TOO_MANY, headers={'Retry-After': '3'})] * 3,
        max_attempts=3)

    with pytest.raises(utils.ApiError) as raised:
        client.get('/v4/managedAreas/ma-1/forestand')

    assert raised.value.status_code == 429
    assert raised.value.code == 'tooManyConcurrentRequests'
    assert raised.value.retry_after == 3
    assert slept == [3, 3]


def test_a_retry_after_that_is_not_a_number_of_seconds_falls_back_to_a_wait_of_our_own():
    client, slept = api(
        FakeResponse(status_code=429, body=TOO_MANY,
                     headers={'Retry-After': 'Wed, 21 Oct 2026 07:28:00 GMT'}),
        FakeResponse(body={'results': []}))

    client.get('/v4/projects', {'teamId': 'team-1'})

    assert slept == [utils.DEFAULT_RETRY_AFTER_SECONDS]


def test_an_error_that_is_not_a_429_is_not_retried():
    client, slept = api(FakeResponse(status_code=404, body={'status': 404, 'code': 'teamNotFound'}))

    with pytest.raises(utils.ApiError):
        client.get('/v4/projects', {'teamId': 'nope'})

    assert slept == []


def test_a_retried_429_sends_the_plan_again_from_the_start_rather_than_a_spent_stream():
    """A streamed body is read to its end by the first attempt, so each attempt needs a fresh one."""
    client, slept = api(
        FakeResponse(status_code=429, body=TOO_MANY, headers={'Retry-After': '1'}),
        FakeResponse(status_code=201, body={'importId': 'imp-1', 'managedAreaIds': []}))
    session = client.session
    opened = []

    def fresh_plan():
        plan = io.BytesIO(b'<forestand>plan</forestand>')
        opened.append(plan)
        return plan

    client.post_xml('/v4/teams/team-1/forestand', fresh_plan)

    assert len(opened) == 2, 'the plan should be opened once per attempt'
    assert session.calls[1]['data'] is opened[1]
    assert session.calls[1]['data'].read() == b'<forestand>plan</forestand>'
