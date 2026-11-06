"""Shared helpers for the Global Forester API V4 example scripts."""

import json
import os
import pathlib
import time
import uuid

import requests

CLIENT_ID = 'clientId'
CLIENT_SECRET = 'clientSecret'
HOST = 'https://api.globalforester.com'
TOKEN_URL = 'https://auth2.globalforester.com/oauth2/token'

# How long to wait when a 429 did not say, or said it as a date we do not read.
DEFAULT_RETRY_AFTER_SECONDS = 10

# How many times a call is waited out and tried again before the caller is told about it.
MAX_ATTEMPTS = 4

# How long to wait for an answer, as (connect, read). The gateway answers 504 after 180s, so
# waiting longer than it does buys nothing; waiting forever, which is what requests does when it
# is given no timeout, is the one thing a script must not do.
REQUEST_TIMEOUT_SECONDS = (10, 180)

# Asking again under a key whose call has not answered yet: how long between asks, and how long to
# keep it up. An import is given ten minutes on the server, and the key is held a little longer
# than that, so one still running after this is asked about later rather than waited out here.
IN_PROGRESS_WAIT_SECONDS = 10
IN_PROGRESS_BUDGET_SECONDS = 600


def new_idempotency_key():
    """A fresh key. Keep it for as long as the retries may go on: a new key is a new call."""
    return str(uuid.uuid4())


def host():
    """Set GF_API_HOST to point the scripts at test instead of production."""
    return os.environ.get('GF_API_HOST', HOST)


def token_url():
    """Follows the environment, so set it together with GF_API_HOST."""
    return os.environ.get('GF_TOKEN_URL', TOKEN_URL)


def credentials():
    """The environment wins over this file, so a shared checkout needs no edit."""
    return (
        os.environ.get('GF_CLIENT_ID', CLIENT_ID),
        os.environ.get('GF_CLIENT_SECRET', CLIENT_SECRET))


def get_access_token():
    """Exchanges the client credentials for an access token."""
    client_id, client_secret = credentials()

    response = requests.post(
        token_url(),
        params={'grant_type': 'client_credentials'},
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        auth=requests.auth.HTTPBasicAuth(client_id, client_secret))
    response.raise_for_status()

    return response.json()['access_token']


def client():
    """The Api the scripts use: the configured environment, with a fresh access token."""
    return Api(host=host(), token=get_access_token())


class ApiError(Exception):
    """An error answer from V4.

    Act on ``code`` rather than on the wording of ``detail``. Some codes bring extra fields with
    them, and they are all kept in ``problem``.
    """

    def __init__(self, status_code, problem=None, retry_after=None):
        self.status_code = status_code
        self.problem = problem or {}
        self.code = self.problem.get('code')
        self.detail = self.problem.get('detail', '')
        self.retry_after = retry_after

        super().__init__(' '.join(str(part) for part in (status_code, self.code, self.detail) if part))


class NoAnswer(ApiError):
    """No answer came back: the read timed out, or a gateway gave up with 504.

    Nothing is known about what happened at the other end, and an import goes on running there
    whether or not anyone is still listening. A call made under an idempotencyKey is therefore
    asked again with that same key; a new one would run the whole thing a second time.

    It is an ApiError, so a script that handles those already handles this one too.
    """

    def __init__(self, status_code=None, detail=''):
        super().__init__(status_code, {'detail': detail})


class Api:
    """Talks to /v4. Every call goes through here, so the paging and the retries live in one place."""

    def __init__(self, host=None, token=None, session=None, sleep=time.sleep,
                 max_attempts=MAX_ATTEMPTS, timeout=REQUEST_TIMEOUT_SECONDS,
                 in_progress_budget=IN_PROGRESS_BUDGET_SECONDS, now=time.monotonic):
        self.host = (host or HOST).rstrip('/')
        self.token = token
        self.session = session or requests.Session()
        self.sleep = sleep
        self.max_attempts = max_attempts
        self.timeout = timeout
        self.in_progress_budget = in_progress_budget
        self.now = now

    def pages(self, path, params=None):
        """Yields one page at a time, following nextPageToken until it is absent.

        The token is opaque: it is sent straight back as pageToken and never built here. A short
        page is not the end of the list, so stop on the missing token rather than on a short page.
        """
        filters = dict(params or {})
        token = None

        while True:
            page = self.get(path, filters if token is None else {**filters, 'pageToken': token})
            yield page

            token = page.get('nextPageToken')
            if not token:
                return

    def items(self, path, params=None):
        """Yields every item of a list, page boundaries hidden."""
        for page in self.pages(path, params):
            yield from page.get('results', [])

    def get(self, path, params=None):
        return self.request('GET', path, params=params).json()

    def delete(self, path):
        """Deletes something. The answer carries no body, so there is nothing to hand back."""
        self.request('DELETE', path)

    def post_json(self, path, body, params=None):
        return self.request(
            'POST',
            path,
            params=params,
            data=json.dumps(body),
            headers={'Content-Type': 'application/json'}).json()

    def post_xml(self, path, body_factory, params=None):
        """Sends raw Forestand XML as the request body, never a multipart upload.

        The body is handed over as a function because a retry has to send the plan again from the
        start, and a stream the first attempt read is spent.
        """
        return self.request(
            'POST',
            path,
            params=params,
            body_factory=body_factory,
            headers={'Content-Type': 'application/xml'}).json()

    def create(self, path, body, idempotency_key=None):
        """Creates something, retrying safely under an idempotencyKey."""
        return self.retry_under_key(
            lambda params: self.post_json(path, body, params=params), idempotency_key)

    def create_from_xml(self, path, body_factory, idempotency_key=None):
        """Sends a Forestand plan, retrying safely under an idempotencyKey."""
        return self.retry_under_key(
            lambda params: self.post_xml(path, body_factory, params=params), idempotency_key)

    def retry_under_key(self, call, idempotency_key):
        """Makes a call under an idempotencyKey, which travels as a query parameter.

        Three answers mean the call may still be running, and all three are met the same way: ask
        again with the same key. 409 idempotencyKeyInProgress says so outright; a 504 and a call
        that never answered say nothing at all, and the work behind them carries on regardless.
        Asking is kept up for IN_PROGRESS_BUDGET_SECONDS rather than for a few attempts, because
        an import takes minutes rather than seconds.

        409 idempotencyKeyReused is the one that is not retried: the key is spoken for by a
        different request, and only a new key fixes that.
        """
        params = {'idempotencyKey': idempotency_key} if idempotency_key else {}
        if not idempotency_key:
            return call(params)

        giving_up_at = self.now() + self.in_progress_budget

        while True:
            try:
                return call(params)
            except ApiError as error:
                if not self.may_still_be_running(error) or self.now() >= giving_up_at:
                    raise

                print(f'No answer yet under this key ({error}). Waiting '
                      f'{IN_PROGRESS_WAIT_SECONDS}s and asking again with the same key.')
                self.sleep(IN_PROGRESS_WAIT_SECONDS)

    @staticmethod
    def may_still_be_running(error):
        """Whether the call behind this error may be going on at the other end."""
        return isinstance(error, NoAnswer) or error.code == 'idempotencyKeyInProgress'

    def download(self, path, destination, params=None):
        """Writes a download to a file in chunks, so a whole plan or picture is never held in memory."""
        destination = pathlib.Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)

        response = self.request('GET', path, params=params, stream=True)
        try:
            with open(destination, 'wb') as output:
                for chunk in response.iter_content(chunk_size=65536):
                    output.write(chunk)
        finally:
            response.close()

        return destination

    def request(self, method, path, params=None, headers=None, body_factory=None, **kwargs):
        """Makes one call, waiting out a 429 for the seconds Retry-After asks for.

        Only a 429 is retried: it means the server is busy, and the one thing to do about it is to
        wait and ask again. Every other error is the caller's to deal with, and a call that never
        answered becomes a NoAnswer rather than a requests exception.
        """
        for attempt in range(1, self.max_attempts + 1):
            if body_factory is not None:
                kwargs['data'] = body_factory()

            try:
                response = self.session.request(
                    method,
                    f'{self.host}{path}',
                    params=params,
                    headers={'Authorization': f'Bearer {self.token}', **(headers or {})},
                    timeout=self.timeout,
                    **kwargs)
            except (requests.Timeout, requests.ConnectionError) as broke_off:
                raise NoAnswer(
                    detail=f'No answer within {self.timeout[1]}s: {broke_off}') from broke_off

            # A gateway that gave up is not the API saying no. What it was waiting for may well
            # have gone through, which is what makes this different from every other error here.
            if response.status_code == 504:
                raise NoAnswer(504, 'A gateway gave up waiting for the answer.')

            if response.status_code < 400:
                return response

            error = ApiError(
                response.status_code,
                self.problem_of(response),
                retry_after=self.retry_after_of(response))

            if error.status_code != 429 or attempt == self.max_attempts:
                raise error

            print(f'Busy. Waiting {error.retry_after}s before asking again '
                  f'(attempt {attempt} of {self.max_attempts}).')
            self.sleep(error.retry_after)

    @staticmethod
    def retry_after_of(response):
        """The seconds a 429 asks us to wait.

        HTTP also allows a date, which we do not read; a wait of our own stands in for it rather
        than letting the caller retry straight away.
        """
        if response.status_code != 429:
            return None

        try:
            return int(response.headers.get('Retry-After', ''))
        except ValueError:
            return DEFAULT_RETRY_AFTER_SECONDS

    @staticmethod
    def problem_of(response):
        """The ProblemDetails behind an error answer, or nothing when the body is not one."""
        try:
            problem = response.json()
        except Exception:
            return None

        return problem if isinstance(problem, dict) else None
