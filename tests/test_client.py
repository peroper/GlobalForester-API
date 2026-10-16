import utils


def test_the_host_and_token_url_come_from_the_environment_so_test_needs_no_code_change(monkeypatch):
    monkeypatch.setenv('GF_API_HOST', 'https://api.test.globalforester.com')
    monkeypatch.setenv('GF_TOKEN_URL', 'https://auth2.test.globalforester.com/oauth2/token')

    assert utils.host() == 'https://api.test.globalforester.com'
    assert utils.token_url() == 'https://auth2.test.globalforester.com/oauth2/token'


def test_without_the_environment_the_scripts_talk_to_production(monkeypatch):
    monkeypatch.delenv('GF_API_HOST', raising=False)
    monkeypatch.delenv('GF_TOKEN_URL', raising=False)

    assert utils.host() == utils.HOST
    assert utils.token_url() == utils.TOKEN_URL


def test_the_credentials_can_come_from_the_environment_instead_of_the_file(monkeypatch):
    monkeypatch.setenv('GF_CLIENT_ID', 'id-from-env')
    monkeypatch.setenv('GF_CLIENT_SECRET', 'secret-from-env')

    assert utils.credentials() == ('id-from-env', 'secret-from-env')
