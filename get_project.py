"""Reads one Project, its links and its Tracklogs.

The Project answer carries type and status, and only links that lead somewhere: changeSummary is
there exactly when there is a change summary to read, so follow the link rather than guessing.
"""

import argparse
import json

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='Id of the Project to read.', required=True)
args = parser.parse_args()

api = utils.client()

try:
    project = api.get(f'/v4/projects/{args.project_id}')
except utils.ApiError as error:
    print(f'Could not read the project: {error.code} - {error.detail}')
    raise SystemExit(1)

print(json.dumps(project, indent=2))

links = project.get('links', {})
print('\nLinks on this project:')
for name, path in links.items():
    print(f'  {name}: {path}')

if 'changeSummary' not in links:
    print('  (no changeSummary: this is not a Planuppdatering that is still being worked on)')

print('\nTracklogs:')
try:
    for tracklog in api.items('/v4/tracklogs', {'projectId': args.project_id}):
        if tracklog.get('deleted'):
            continue
        print(f"  {tracklog['id']}  {tracklog.get('name')}  "
              f"geometry={tracklog.get('geometry', {}).get('type')}")
except utils.ApiError as error:
    print(f'Could not list the tracklogs: {error.code} - {error.detail}')
    raise SystemExit(1)
