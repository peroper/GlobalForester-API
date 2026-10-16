"""A stand-in for requests.Session that answers from a scripted list of responses."""

class FakeResponse:
    def __init__(self, status_code=200, body=None, headers=None, content=b''):
        self.status_code = status_code
        self._body = body
        self.headers = headers or {}
        self.content = content

    def json(self):
        if self._body is None:
            raise ValueError('no json body')
        return self._body

    def iter_content(self, chunk_size=1):
        for start in range(0, len(self.content), chunk_size):
            yield self.content[start:start + chunk_size]

    def close(self):
        pass


class FakeSession:
    """Records what was asked, so a test can check the parameters a helper sent."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append({'method': method, 'url': url, **kwargs})
        if not self.responses:
            raise AssertionError(f'No response scripted for {method} {url}')
        return self.responses.pop(0)
