from fake_session import FakeResponse, FakeSession

import utils


def test_pages_follows_the_token_until_it_is_absent():
    session = FakeSession([
        FakeResponse(body={'results': [{'id': 'a'}], 'nextPageToken': 'tok-1'}),
        FakeResponse(body={'results': [{'id': 'b'}], 'nextPageToken': 'tok-2'}),
        FakeResponse(body={'results': [{'id': 'c'}]}),
    ])
    api = utils.Api(host='https://api.test', token='t', session=session)

    ids = [item['id'] for item in api.items('/v4/projects', {'teamId': 'team-1'})]

    assert ids == ['a', 'b', 'c']


def test_pages_sends_the_token_back_as_pagetoken_and_keeps_the_other_filters():
    session = FakeSession([
        FakeResponse(body={'results': [], 'nextPageToken': 'tok-1'}),
        FakeResponse(body={'results': []}),
    ])
    api = utils.Api(host='https://api.test', token='t', session=session)

    list(api.pages('/v4/projects', {'teamId': 'team-1'}))

    assert session.calls[0]['params'] == {'teamId': 'team-1'}
    assert session.calls[1]['params'] == {'teamId': 'team-1', 'pageToken': 'tok-1'}


def test_a_short_page_is_not_the_end_of_the_list():
    """The server may hand back fewer items than asked for while more exist."""
    session = FakeSession([
        FakeResponse(body={'results': [{'id': 'a'}], 'nextPageToken': 'tok-1'}),
        FakeResponse(body={'results': [{'id': 'b'}, {'id': 'c'}]}),
    ])
    api = utils.Api(host='https://api.test', token='t', session=session)

    ids = [item['id'] for item in api.items('/v4/projects', {'teamId': 'team-1', 'pageSize': 100})]

    assert ids == ['a', 'b', 'c']
