"""Imports a Forestand plan into an Arbetsgrupp, one Område per skifte.

The plan is the request body as application/xml. There is no file upload and no name: the body is
streamed from disk, so a large plan is never read into memory here either.

An import always creates. Nothing is matched against what is already there, so running this twice
with two different keys gives you the Områden twice. That is what the idempotencyKey is for: ask
again with the same key and the same plan and you get the first answer back instead of a second
import. The key covers the Arbetsgrupp as well, so the same plan and key aimed at another one is
refused rather than imported.

Which answer came back decides what to do next:

  No answer, or 504   The import is most likely still running and finishes on its own. Ask again
                      with the same key - the helper does that for you for ten minutes, and
                      --key picks it up again after that. Never take a new key here.
  500                 It failed on our side, and the failure is remembered under the key. An
                      import is not one transaction, so part of the plan may be in place: look at
                      the Arbetsgrupp's Områden before sending it again, and take a new key.
  429                 Only a few imports run at once. The helper waits out Retry-After.

The plan has to be reopened for each attempt, which is why the body is handed over as a function
rather than an open stream.
"""

import argparse
import os

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t', '--team', dest='team_id', help='Id of the Arbetsgrupp to import the plan into.', required=True)
parser.add_argument('-p', '--path', dest='path', help='Path to the Forestand XML file to import.', required=True)
parser.add_argument('-k', '--key', dest='idempotency_key', help='An idempotencyKey to use instead of a fresh one, to retry an earlier import.')
args = parser.parse_args()

api = utils.client()

key = args.idempotency_key or utils.new_idempotency_key()
print(f'idempotencyKey: {key}')
print('Keep it: if you never see an answer, ask again with this key and the same plan.')
print(f'Sending {os.path.getsize(args.path)} bytes from {args.path}.')

# One open file per attempt, closed once the import has answered.
plans = []


def plan():
    plans.append(open(args.path, 'rb'))
    return plans[-1]


try:
    imported = api.create_from_xml(
        f'/v4/teams/{args.team_id}/forestand', plan, idempotency_key=key)
except utils.NoAnswer as no_answer:
    print(f'\nStill no answer after asking under the same key for '
          f'{utils.IN_PROGRESS_BUDGET_SECONDS}s. ({no_answer})')
    print(f'The import is most likely still running. Ask again later with --key {key}: while it '
          f'runs you get idempotencyKeyInProgress, and once it is done that key hands you the '
          f'answer. The API keeps it for 24 hours.')
    raise SystemExit(1)
except utils.ApiError as error:
    if error.code == 'planTooLarge':
        print(f'The plan is too large to import. ({error.detail})')
    elif error.code == 'invalidForestand':
        print(f'That body is not a plan we can import. A plan must hold at least one skifte. ({error.detail})')
    elif error.code == 'tooManyConcurrentRequests':
        print(f'The server is still busy after several tries. '
              f'It last asked us to wait {error.retry_after}s. Try again later with the same key.')
    elif error.code == 'idempotencyKeyInProgress':
        print(f'The import under this key is still running. Ask again later with --key {key}. '
              f'({error.detail})')
    elif error.code == 'idempotencyKeyReused':
        print(f'That key is already used for a different plan, or for this plan into another '
              f'Arbetsgrupp. Run again without --key. ({error.detail})')
    elif error.status_code == 500:
        print('The import failed on our side. Part of the plan may be in place: look at the '
              "Arbetsgrupp's Områden before sending it again, and take a new key when you do.")
    else:
        print(f'Could not import the plan: {error.code} - {error.detail}')
    raise SystemExit(1)
finally:
    for opened in plans:
        opened.close()

print(f"\nImport {imported['importId']} created {len(imported['managedAreaIds'])} Område(n):")
for managed_area_id in imported['managedAreaIds']:
    print(f'  {managed_area_id}')
