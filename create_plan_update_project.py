"""Creates a Planuppdatering (forestManagementPlanning), safely retryable under an idempotencyKey.

A Planuppdatering covers one Område, so managedAreaId is required and must belong to the same
Arbetsgrupp. The answer carries managedAreaWorkingCopyId: the Arbetskopia of the Område that this
Project edits, written back to the master when the Uppgift is completed in the app.

Every project type but scout is behind a feature flag. You need it switched on, and so does the
person you hand the Uppgift to; otherwise the answer is 403 with code projectTypeNotEnabled, the
projectType and a subject of caller or assignee. The flag's internal name is never shown - ask your
Global Forester contact to have it switched on.
"""

import argparse

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t', '--team', dest='team_id', help='Id of the Arbetsgrupp to create the Project in.', required=True)
parser.add_argument('-n', '--name', dest='name', help='Name of the new Project.', required=True)
parser.add_argument('-m', '--managed-area', dest='managed_area_id', help='Id of the Område the Planuppdatering covers.', required=True)
parser.add_argument('-a', '--assigned-to', dest='assigned_to_id', help='Id of the Arbetsgrupp member who gets the Uppgift.')
parser.add_argument('-k', '--key', dest='idempotency_key', help='An idempotencyKey to use instead of a fresh one, to retry an earlier call.')
args = parser.parse_args()

api = utils.client()

key = args.idempotency_key or utils.new_idempotency_key()
print(f'idempotencyKey: {key}')

body = {
    'teamId': args.team_id,
    'name': args.name,
    'type': 'forestManagementPlanning',
    'managedAreaId': args.managed_area_id}
if args.assigned_to_id:
    body['assignedToId'] = args.assigned_to_id

try:
    project = api.create('/v4/projects', body, idempotency_key=key)
except utils.ApiError as error:
    if error.code == 'projectTypeNotEnabled':
        who = 'you' if error.problem.get('subject') == 'caller' else 'the person you assigned to'
        print(f"Project type {error.problem.get('projectType')} is not switched on for {who}. "
              f'Ask your Global Forester contact to enable it.')
    elif error.code == 'managedAreaNotFound':
        print(f'That Område is not available to you, or does not belong to that Arbetsgrupp. ({error.detail})')
    elif error.code == 'idempotencyKeyReused':
        print(f'That key is already used for a different body. Run again without --key. ({error.detail})')
    else:
        print(f'Could not create the project: {error.code} - {error.detail}')
    raise SystemExit(1)

print(f"\nCreated project {project['id']}: {project['name']} "
      f"(type={project['type']}, status={project['status']})")
print(f"Arbetskopia of the Område: {project['managedAreaWorkingCopyId']}")
print(f"Change summary: {project.get('links', {}).get('changeSummary')}")
