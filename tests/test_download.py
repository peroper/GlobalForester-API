import pytest
from fake_session import FakeResponse, FakeSession

import utils


def test_a_download_is_written_to_the_path_in_chunks_rather_than_held_in_memory(tmp_path):
    session = FakeSession([FakeResponse(content=b'<forestand>plan</forestand>')])
    api = utils.Api(host='https://api.test', token='t', session=session)
    destination = tmp_path / 'plan.xml'

    written = api.download('/v4/managedAreas/ma-1/forestand', destination)

    assert written == destination
    assert destination.read_bytes() == b'<forestand>plan</forestand>'
    assert session.calls[0]['stream'] is True


def test_a_download_that_is_refused_raises_rather_than_writing_an_error_body_to_the_file(tmp_path):
    session = FakeSession([FakeResponse(status_code=404, body={'status': 404, 'code': 'fileNotFound'})])
    api = utils.Api(host='https://api.test', token='t', session=session)
    destination = tmp_path / 'picture.jpg'

    with pytest.raises(utils.ApiError) as raised:
        api.download('/v4/files/f-1', destination)

    assert raised.value.code == 'fileNotFound'
    assert not destination.exists()
