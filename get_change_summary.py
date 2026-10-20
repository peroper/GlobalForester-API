"""Reads what completing a Planuppdatering would change in the master plan.

Only a forestManagementPlanning Project that is still being worked on has a change summary. The
Project itself tells you whether to ask: the link changeSummary is there exactly when there is one
to read, so this script follows the link instead of guessing.

The counting is literal, against the master plan. Splitting one stand into two shows as one stand
removed and two created, and the treatments beneath them to match - never as one stand changed. The
planning treatment that every Planuppdatering opens with always counts as one created treatment.
Nothing is written and no history is kept, so the answer can differ from one call to the next as the
field work goes on.
"""

import argparse

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='Id of the Planuppdatering to read the change summary for.', required=True)
args = parser.parse_args()

api = utils.client()

try:
    project = api.get(f'/v4/projects/{args.project_id}')
except utils.ApiError as error:
    print(f'Could not read the project: {error.code} - {error.detail}')
    raise SystemExit(1)

if 'changeSummary' not in project.get('links', {}):
    print(f"Project {project['id']} has no change summary "
          f"(type={project['type']}, status={project['status']}). "
          f'Only a forestManagementPlanning project that is still being worked on has one.')
    raise SystemExit(0)

try:
    summary = api.get(f"/v4/projects/{args.project_id}/changeSummary")
except utils.ApiError as error:
    if error.code == 'changeSummaryNotAvailable':
        print(f'The change summary is gone after all: {error.detail}')
    else:
        print(f'Could not read the change summary: {error.code} - {error.detail}')
    raise SystemExit(1)

print(f"Completing {project['name']} would change the master plan as follows:\n")
for kind in ('compartments', 'actions', 'factors'):
    counts = summary[kind]
    print(f"  {kind:<14} created {counts['created']:>4}   "
          f"changed {counts['updated']:>4}   removed {counts['deleted']:>4}")

print(f"\n  Stands touched at all: {summary['affectedCompartments']}")
