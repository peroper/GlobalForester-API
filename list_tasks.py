"""Lists Uppgifter for an Arbetsgrupp, a Project or one person.

At least one of --team, --project and --assigned-to is required: there is no list of every Uppgift
in the organisation. Giving several narrows the list to the Uppgifter that match all of them.

The answer carries completionError when a Slutförande has failed. The status alone does not tell
you: after a failure an Uppgift can stay sent, go back to in progress, or be interrupted.
"""

import argparse

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t', '--team', dest='team_id', help='Id of the Arbetsgrupp to list Uppgifter for.')
parser.add_argument('-p', '--project', dest='project_id', help='Id of the Project to list Uppgifter for.')
parser.add_argument('-a', '--assigned-to', dest='assigned_to_id', help='Id of the person to list Uppgifter for.')
parser.add_argument('-d', '--include-deleted', dest='include_deleted', help='Also list Uppgifter that have been deleted.', action='store_true')
args = parser.parse_args()

if not (args.team_id or args.project_id or args.assigned_to_id):
    parser.error('Give at least one of --team, --project and --assigned-to.')

api = utils.client()

params = {}
if args.team_id:
    params['teamId'] = args.team_id
if args.project_id:
    params['projectId'] = args.project_id
if args.assigned_to_id:
    params['assignedToId'] = args.assigned_to_id
if args.include_deleted:
    params['includeDeleted'] = 'true'

try:
    for task in api.items('/v4/tasks', params):
        if task.get('deleted'):
            print(f"{task['id']}  (deleted)")
            continue

        line = (f"{task['id']}  project={task['projectId']}  "
                f"type={task['taskType']}  status={task['status']}  "
                f"assignedTo={task.get('assignedToName') or 'Otilldelad (unassigned)'}")
        if task.get('completionError'):
            line += f"  completionError={task['completionError']}"
        print(line)
except utils.ApiError as error:
    print(f'Could not list tasks: {error.code} - {error.detail}')
