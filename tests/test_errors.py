import pytest
from fake_session import FakeResponse, FakeSession

import utils


def api(*responses, **kwargs):
    return utils.Api(host='https://api.test', token='t', session=FakeSession(responses), **kwargs)


def test_a_problem_details_answer_becomes_an_api_error_carrying_the_stable_code():
    client = api(FakeResponse(
        status_code=404,
        body={'status': 404, 'detail': 'No project with id p-1 is available to you.',
              'code': 'projectNotFound'}))

    with pytest.raises(utils.ApiError) as raised:
        client.get('/v4/projects/p-1')

    assert raised.value.status_code == 404
    assert raised.value.code == 'projectNotFound'
    assert 'p-1' in raised.value.detail


def test_a_switched_off_project_type_keeps_the_extra_fields_the_caller_acts_on():
    client = api(FakeResponse(
        status_code=403,
        body={'status': 403, 'detail': 'Project type forestManagementPlanning is not enabled for you.',
              'code': 'projectTypeNotEnabled', 'projectType': 'forestManagementPlanning',
              'subject': 'caller'}))

    with pytest.raises(utils.ApiError) as raised:
        client.post_json('/v4/projects', {'teamId': 'team-1', 'name': 'x'})

    assert raised.value.code == 'projectTypeNotEnabled'
    assert raised.value.problem['subject'] == 'caller'


def test_an_error_without_a_problem_details_body_still_becomes_an_api_error():
    client = api(FakeResponse(status_code=502, body=None))

    with pytest.raises(utils.ApiError) as raised:
        client.get('/v4/projects/p-1')

    assert raised.value.status_code == 502
    assert raised.value.code is None
