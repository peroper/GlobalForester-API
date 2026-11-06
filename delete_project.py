"""Deletes a Project and everything under it.

Everything the Project owns goes with it: its Uppgifter, its tracklogs and, for a Planuppdatering,
the Arbetskopia of the Område and the work done on it. The Område itself belongs to the
Arbetsgrupp and stays as it was, so a Planuppdatering deleted before it was completed leaves no
trace in the plan.

Deleting is marking. The Project is gone from the list, and list_projects.py --include-deleted
still names it, carrying deleted: true and nothing but its id and the audit fields. Deleting one
that is already deleted gives 404, as does one you cannot reach.

There is no idempotencyKey here. Nothing is created, so asking twice costs nothing: the second
call answers 404.
"""

import argparse

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='Id of the Project to delete.', required=True)
parser.add_argument('-y', '--yes', dest='yes', help='Delete without asking first.', action='store_true')
args = parser.parse_args()

api = utils.client()

try:
    project = api.get(f'/v4/projects/{args.project_id}')
except utils.ApiError as error:
    if error.code == 'projectNotFound':
        print(f'No project with that id is available to you. ({error.detail})')
    else:
        print(f'Could not read the project: {error.code} - {error.detail}')
    raise SystemExit(1)

print(f"About to delete {project['id']}: {project['name']} "
      f"(type={project['type']}, status={project['status']})")

if not args.yes and input('Delete it, with its Uppgifter and tracklogs? [y/N] ').strip().lower() != 'y':
    print('Left alone.')
    raise SystemExit(0)

try:
    api.delete(f'/v4/projects/{args.project_id}')
except utils.ApiError as error:
    if error.code == 'projectNotFound':
        print(f'It is gone already, or no longer available to you. ({error.detail})')
    else:
        print(f'Could not delete the project: {error.code} - {error.detail}')
    raise SystemExit(1)

print(f"Deleted {project['id']}. list_projects.py --include-deleted still names it.")
