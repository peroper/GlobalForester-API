"""Lists an Arbetsgrupp's Projects, one page at a time.

Shows how a V4 list is read: follow nextPageToken until it is absent. The token is opaque, so send
it straight back and never build one yourself. pageSize is a wish - the server decides and may hand
back fewer items than asked for even when more exist, so a short page is not the end of the list.

With --include-deleted the list also carries Projects that have been deleted. A deleted Project is
only named: it has deleted: true, its id and the audit fields, and none of the rest.
"""

import argparse

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t', '--team', dest='team_id', help='Id of the Arbetsgrupp to list Projects for.', required=True)
parser.add_argument('-s', '--page-size', dest='page_size', type=int, help='How many items to ask for per page. Default 100, at most 500.')
parser.add_argument('-d', '--include-deleted', dest='include_deleted', help='Also list Projects that have been deleted.', action='store_true')
args = parser.parse_args()

api = utils.client()

params = {'teamId': args.team_id}
if args.page_size:
    params['pageSize'] = args.page_size
if args.include_deleted:
    params['includeDeleted'] = 'true'

try:
    for page_number, page in enumerate(api.pages('/v4/projects', params), start=1):
        results = page.get('results', [])
        print(f'\nPage {page_number}: {len(results)} project(s)')

        for project in results:
            if project.get('deleted'):
                print(f"  {project['id']}  (deleted, last changed {project['updated']})")
            else:
                print(f"  {project['id']}  {project['name']}  "
                      f"type={project['type']}  status={project['status']}  updated={project['updated']}")

        if 'nextPageToken' not in page:
            print('\nNo more pages.')
except utils.ApiError as error:
    print(f'Could not list projects: {error.code} - {error.detail}')
    raise SystemExit(1)
