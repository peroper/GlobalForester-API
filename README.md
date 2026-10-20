# Global Forester API Example Scripts

This repository contains a collection of Python scripts intended as a starting point for developers
looking to utilize the Global Forester API using Python. These scripts can be used or combined
as-is, or serve as inspiration for more complex implementations.

See <https://api.globalforester.com/swagger> for more detailed information about the API.

The examples use **version 4** of the API, which is the recommended version. V4 adds reading and
creating Projects with their type and status, Forestand export and import, and reading Uppgifter and
their Påverkansfaktorer. Examples for
[version 3](https://api.globalforester.com/swagger/index.html?urls.primaryName=V3) can be found
[here](https://github.com/peroper/GlobalForester-API/tree/3.0), and for
[version 2](https://api.globalforester.com/swagger/index.html?urls.primaryName=V2)
[here](https://github.com/peroper/GlobalForester-API/tree/2.0). Version 1 of the API has ceased to be
and is now history.

The scripts call `/v4` directly with [requests](https://requests.readthedocs.io) rather than through
a generated client. Reading a `Retry-After` header, streaming a plan as the request body and acting
on an error `code` are all clearer that way, and there is no code generation step to run.

## Getting Started

### 1. Clone the repo

```shell
git clone https://github.com/peroper/GlobalForester-API.git
cd GlobalForester-API
```

### 2. Install Python 3

<https://www.python.org>

### 3. Install Python Dependencies

It is recommended to install dependencies in a virtual environment. This will isolate project
dependencies from other projects on the same computer. If you want to read more about virtual
environments you can do so here: <https://docs.python.org/3/library/venv.html>

1. Create a virtual environment

   ```shell
   python3 -m venv venv
   ```

2. Activate the virtual environment

   ```shell
   source venv/bin/activate
   ```

3. Install dependencies

   ```shell
   pip3 install -r requirements.txt
   ```

### 4. Enter your credentials

Enter your client ID and client secret in _utils.py_, or set them in the environment:

```shell
export GF_CLIENT_ID=... GF_CLIENT_SECRET=...
```

[Contact support](https://www.globalforester.com/manual/basics#errors-and-support) if you don't have
a client ID and client secret and API access is included in your Global Forester subscription.

To run against the test environment instead of production, point the scripts at it:

```shell
export GF_API_HOST=https://api.test.globalforester.com
export GF_TOKEN_URL=https://auth2.test.globalforester.com/oauth2/token
```

### 5. Run Scripts

```shell
python3 name_of_script.py
```

To get more information about a script, run:

```shell
python3 name_of_script.py -h
```

## The scripts

| Script | What it shows |
| --- | --- |
| `list_projects.py` | Reading a list with token paging, and `includeDeleted` |
| `get_project.py` | One Project, the links on it, and its Tracklogs |
| `create_scout_project.py` | Creating a scout Project with an `idempotencyKey` |
| `create_plan_update_project.py` | Creating a Planuppdatering, and the feature flag behind it |
| `get_change_summary.py` | What completing a Planuppdatering would change in the master plan |
| `list_tasks.py` | Uppgifter per Arbetsgrupp, Project or person |
| `get_task_factors.py` | An Uppgift's Påverkansfaktorer and their pictures |
| `export_forestand.py` | Exporting an Område's plan as Forestand XML |
| `import_forestand.py` | Importing a Forestand plan, one Område per skifte |
| `poll_rapid_orthophotos.py` | Polling a list for changes, and the gap that comes with it |
| `download_rapid_orthophoto_files_for_project.py` | Downloading what a drone flight produced |

The shared helpers live in `utils.py`: the access token, the paging loop, the `Retry-After` waits
and turning an error answer into an exception that carries the API's stable `code`.

## Reading a list: token paging

Every V4 list is read one page at a time. A page carries `results` and, when there is more to read,
a `nextPageToken`:

```json
{ "results": [ ... ], "nextPageToken": "eyJ1cGRhdGVkIjoi..." }
```

Send that token back as `pageToken` on the next call, keeping your other filters, and keep going
until a page comes back **without** a token. That is the end of the list.

Three things to know:

- **The token is opaque.** Send back exactly what you were given. Do not read it, build one, or
  carry one over from a different endpoint — a token that is not ours gives 400 with
  `code: pageTokenNotReadable`.
- **`pageSize` is a wish.** The server decides and may hand back fewer items than you asked for even
  when more exist. **Stop on the missing token, never on a short page.** The default is 100 and the
  most you can ask for is 500.
- **An item can come back twice.** A record changed while you were paging can appear again on a
  later page. The later copy is the current one.

Lists are ordered by `updated` and id, oldest change first. `includeDeleted=true` also brings back
records that have been deleted; a deleted record is only named, carrying `deleted: true`, its id and
the audit fields and nothing else.

### Polling for changes

The token is **not** a "carry on from here next time" marker. It names a position inside a list you
are reading, and the last page carries no token at all, so when you reach the end of a list there is
nothing left to save. V4 also has no `updatedAfter`.

So polling means sweeping the whole list each time — token paging carries you through it — and
comparing against the newest `updated` your last run saw. Lists are ordered by `updated`, so the
changes are at the end.

### The known gap: records that sync late

That comparison can miss something. The app works offline, and a record it syncs late arrives
carrying the `updated` it had when the field worker *saved* it, not the time it reached us. That can
be older than the mark from your last run, so the record sorts in behind it and your comparison
quietly skips it — for good, because it will never look newer than the mark either.

> **If you poll for changes, ignore your mark now and then and take everything the sweep found —
> once a day is usually enough.**

`poll_rapid_orthophotos.py` shows both: it keeps the mark between runs, and `--all` ignores it.

## Retrying safely: `idempotencyKey`

Creating a Project and importing a plan both take an `idempotencyKey` — **as a query parameter, not
as a field in the body**. Make up a key of your own, keep it, and if you never see an answer, ask
again with the same key and the same body. You get the first answer back instead of a second Project
or a second import. The key is yours alone and the API keeps the answer under it for 24 hours. A
failure is remembered too, so a retry gets the same failure rather than a second attempt.

Two different 409s can come back, and the `code` tells them apart because you act differently on
each:

| `code` | What happened | What to do |
| --- | --- | --- |
| `idempotencyKeyInProgress` | The first call under this key has not answered yet | Wait a moment and ask again **with the same key** |
| `idempotencyKeyReused` | The key is already used for a *different* body | Pick a **new** key |

`utils.py` waits out the first one for you and raises the second, since only you can decide what the
new call should be. An import is not one transaction, so after a failed import pick a new key rather
than retrying the old one.

## When the server is busy: 429 and `Retry-After`

Forestand export and import are heavy, so only a few run at once — a couple per caller and a few per
server. Beyond that the answer is 429 with `code: tooManyConcurrentRequests` and a `Retry-After`
header saying how many seconds to wait:

```
HTTP/1.1 429 Too Many Requests
Retry-After: 10
```

Wait that many seconds and ask again. Do not retry immediately and do not retry forever. `utils.py`
does this for every call: it waits out the seconds in `Retry-After`, tries a few times, and then
raises so your script can decide. Only a 429 is retried — every other error is yours to handle.

## Errors

Every V4 error is a
[ProblemDetails](https://www.rfc-editor.org/rfc/rfc9457) carrying a stable `code`:

```json
{
  "status": 403,
  "detail": "Project type forestManagementPlanning is not enabled for you.",
  "code": "projectTypeNotEnabled",
  "projectType": "forestManagementPlanning",
  "subject": "caller"
}
```

**Act on `code`, not on the wording of `detail`.** The wording may change; the code will not. Some
codes bring extra fields with them, as `projectTypeNotEnabled` brings `projectType` and `subject`.
In these scripts an error answer becomes a `utils.ApiError` with `code`, `detail`, `status_code` and
the whole `problem`.

Anything you cannot reach answers 404 rather than 403, so an unfamiliar id and one belonging to
someone else look the same.

## Running the tests

The helpers in `utils.py` have tests. They need no network and no credentials:

```shell
pip3 install -r requirements-dev.txt
python3 -m pytest
```
