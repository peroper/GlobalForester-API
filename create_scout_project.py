"""Creates a scout Project, safely retryable under an idempotencyKey.

type may be left out for a scout Project, as in the app. The server always starts a Project as a
draft, so asking for a status gives 400.

The idempotencyKey is a query parameter, not a field in the body. Ask again with the same key and
the same body and you get the first answer back instead of a second Project. Two 409s can come back
and the code tells them apart: idempotencyKeyInProgress means the first call has not answered yet,
so wait and ask again under the same key - the helper does that for you. idempotencyKeyReused means
the key is spoken for by a different body, which only a new key fixes.

Pass --key to reuse a key from an earlier run and watch the API answer with the stored answer, or
refuse the key when the body differs.

With --path the Tracklogs in a json file are added to the new Project. An example is in the
'projects' folder.
"""

import argparse
import json

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t', '--team', dest='team_id', help='Id of the Arbetsgrupp to create the Project in.', required=True)
parser.add_argument('-n', '--name', dest='name', help='Name of the new Project.', required=True)
parser.add_argument('-a', '--assigned-to', dest='assigned_to_id', help='Id of the Arbetsgrupp member who gets the Uppgift. Left out, a user takes it themselves and an API client leaves it unassigned.')
parser.add_argument('-k', '--key', dest='idempotency_key', help='An idempotencyKey to use instead of a fresh one, to retry an earlier call.')
parser.add_argument('-p', '--path', dest='path', help='Relative path to a json with Tracklogs to add to the new Project.')
args = parser.parse_args()

api = utils.client()

key = args.idempotency_key or utils.new_idempotency_key()
print(f'idempotencyKey: {key}')
print('Keep it: asking again with this key and the same body is a retry, a new key is a new project.')

body = {'teamId': args.team_id, 'name': args.name}
if args.assigned_to_id:
    body['assignedToId'] = args.assigned_to_id

try:
    project = api.create('/v4/projects', body, idempotency_key=key)
except utils.ApiError as error:
    if error.code == 'idempotencyKeyReused':
        print(f'That key is already used for a different body. Run again without --key. ({error.detail})')
    elif error.code == 'assigneeNotInTeam':
        print(f'The person you assigned to is not a member of that Arbetsgrupp. ({error.detail})')
    else:
        print(f'Could not create the project: {error.code} - {error.detail}')
    raise SystemExit(1)

print(f"\nCreated project {project['id']}: {project['name']} "
      f"(type={project['type']}, status={project['status']})")

if args.path:
    with open(args.path, 'r') as project_file:
        for tracklog in json.load(project_file).get('tracklogs', []):
            try:
                api.post_json('/v4/tracklogs', {
                    'projectId': project['id'],
                    'name': tracklog['name'],
                    'comment': tracklog.get('comment'),
                    'geometry': tracklog['geometry']})
                print(f"  added tracklog {tracklog['name']}")
            except utils.ApiError as error:
                print(f"  could not add tracklog {tracklog['name']}: {error.code} - {error.detail}")
