import pytest
import requests
from fake_session import FakeClock, FakeResponse, FakeSession

import utils

IN_PROGRESS = {'status': 409, 'code': 'idempotencyKeyInProgress',
               'detail': 'The first request with this idempotencyKey has not answered yet.'}
REUSED = {'status': 409, 'code': 'idempotencyKeyReused',
          'detail': 'idempotencyKey has already been used for a different request.'}


def api(*responses, **kwargs):
    clock = FakeClock()
    session = FakeSession(responses)
    client = utils.Api(
        host='https://api.test', token='t', session=session,
        sleep=clock.sleep, now=clock, **kwargs)
    return client, session, clock.slept


def test_every_idempotency_key_is_a_new_one_within_the_length_the_api_takes():
    keys = {utils.new_idempotency_key() for _ in range(100)}

    assert len(keys) == 100
    assert all(0 < len(key) <= 128 for key in keys)


def test_the_key_travels_as_a_query_parameter_and_not_in_the_body():
    client, session, _ = api(FakeResponse(status_code=201, body={'id': 'p-1'}))

    client.create('/v4/projects', {'teamId': 'team-1', 'name': 'Scout'}, idempotency_key='key-1')

    assert session.calls[0]['params'] == {'idempotencyKey': 'key-1'}
    assert 'idempotencyKey' not in session.calls[0]['data']


def test_a_call_still_running_under_the_same_key_is_waited_out_and_asked_again_with_that_key():
    client, session, slept = api(
        FakeResponse(status_code=409, body=IN_PROGRESS),
        FakeResponse(status_code=201, body={'id': 'p-1'}))

    created = client.create('/v4/projects', {'name': 'Scout'}, idempotency_key='key-1')

    assert created['id'] == 'p-1'
    assert slept == [utils.IN_PROGRESS_WAIT_SECONDS]
    assert session.calls[1]['params'] == {'idempotencyKey': 'key-1'}


def test_a_key_already_used_for_something_else_is_not_retried_because_it_needs_a_new_key():
    client, _, slept = api(FakeResponse(status_code=409, body=REUSED))

    with pytest.raises(utils.ApiError) as raised:
        client.create('/v4/projects', {'name': 'Scout'}, idempotency_key='key-1')

    assert raised.value.code == 'idempotencyKeyReused'
    assert slept == []


def test_a_create_without_a_key_sends_no_idempotency_parameter():
    client, session, _ = api(FakeResponse(status_code=201, body={'id': 'p-1'}))

    client.create('/v4/projects', {'name': 'Scout'})

    assert session.calls[0]['params'] == {}


def test_a_key_that_stays_in_progress_is_given_up_on_rather_than_waited_on_forever():
    """The budget is a stretch of time rather than a count: an import takes minutes."""
    client, _, slept = api(
        *[FakeResponse(status_code=409, body=IN_PROGRESS)] * 4,
        in_progress_budget=2 * utils.IN_PROGRESS_WAIT_SECONDS)

    with pytest.raises(utils.ApiError) as raised:
        client.create('/v4/projects', {'name': 'Scout'}, idempotency_key='key-1')

    assert raised.value.code == 'idempotencyKeyInProgress'
    assert len(slept) == 2, 'waits between attempts, not after the last one'


def test_a_gateway_that_gave_up_is_asked_again_with_the_same_key_rather_than_taken_as_a_failure():
    """A 504 says nothing about the import, which runs on regardless. A new key would run it twice."""
    client, session, slept = api(
        FakeResponse(status_code=504),
        FakeResponse(status_code=409, body=IN_PROGRESS),
        FakeResponse(status_code=201, body={'importId': 'imp-1', 'managedAreaIds': ['ma-1']}))

    imported = client.create_from_xml(
        '/v4/teams/team-1/forestand', lambda: b'<plan/>', idempotency_key='key-1')

    assert imported['importId'] == 'imp-1'
    assert slept == [utils.IN_PROGRESS_WAIT_SECONDS] * 2
    assert [call['params'] for call in session.calls] == [{'idempotencyKey': 'key-1'}] * 3


def test_a_call_that_never_answered_is_asked_again_with_the_same_key():
    client, session, slept = api(
        requests.exceptions.ReadTimeout('timed out'),
        FakeResponse(status_code=201, body={'importId': 'imp-1', 'managedAreaIds': []}))

    client.create_from_xml(
        '/v4/teams/team-1/forestand', lambda: b'<plan/>', idempotency_key='key-1')

    assert slept == [utils.IN_PROGRESS_WAIT_SECONDS]
    assert session.calls[1]['params'] == {'idempotencyKey': 'key-1'}


def test_a_plan_asked_about_again_is_sent_again_from_the_start():
    client, session, _ = api(
        FakeResponse(status_code=504),
        FakeResponse(status_code=201, body={'importId': 'imp-1', 'managedAreaIds': []}))

    client.create_from_xml(
        '/v4/teams/team-1/forestand', lambda: iter([b'<plan/>']), idempotency_key='key-1')

    assert session.calls[0]['data'] is not session.calls[1]['data']


def test_no_answer_at_all_without_a_key_is_an_api_error_the_scripts_already_handle():
    client, _, slept = api(FakeResponse(status_code=504))

    with pytest.raises(utils.NoAnswer) as raised:
        client.get('/v4/projects/p-1')

    assert isinstance(raised.value, utils.ApiError)
    assert raised.value.status_code == 504
    assert raised.value.code is None
    assert slept == []
