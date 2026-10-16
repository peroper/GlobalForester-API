"""Polls for Rapid Orthophotos that have changed since the last run.

V4 has no updatedAfter, and the page token cannot stand in for one: it names a position inside a
list you are reading, and the last page carries no token at all, so there is nothing to save for
next time. Polling is therefore a full sweep of the list - token paging gets you through it - with
the comparison done here, against the newest 'updated' the last run saw. This script keeps that
mark in a small file so it can be run again and again.

Known gap: an orthophoto the app syncs late carries the 'updated' it had when the field worker saved
it, which can be older than the mark, so comparing against the mark hides it for good. Ignore the
mark now and then - once a day is usually enough - by running with --all, which reports everything
the sweep found.
"""

import argparse
import os

import utils

MARK_FILE = '.rapid_orthophoto_mark'

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='Only poll one Project. Left out, every Project you reach is polled.')
parser.add_argument('-a', '--all', dest='report_all', help='Report everything the sweep found, ignoring the mark, to catch records that synced late.', action='store_true')
args = parser.parse_args()

api = utils.client()

mark = None
if os.path.exists(MARK_FILE):
    with open(MARK_FILE, 'r') as mark_file:
        mark = mark_file.read().strip() or None

if args.report_all:
    print('Reporting everything, ignoring the mark.')
elif mark:
    print(f'Reporting what changed after {mark}.')
else:
    print('No mark saved yet: reporting everything.')

params = {}
if args.project_id:
    params['projectId'] = args.project_id

newest = mark
reported = 0
swept = 0

try:
    # The whole list, every run. The token only carries us from page to page within this sweep.
    for orthophoto in api.items('/v4/rapidOrthophotos', params):
        swept += 1
        updated = orthophoto['updated']

        if newest is None or updated > newest:
            newest = updated

        if mark is not None and not args.report_all and updated <= mark:
            continue

        reported += 1
        state = '(deleted)' if orthophoto.get('deleted') else orthophoto.get('name')
        print(f"{orthophoto['id']}  {state}  "
              f"project={orthophoto.get('projectId')}  updated={updated}")
except utils.ApiError as error:
    print(f'Could not poll orthophotos: {error.code} - {error.detail}')
    raise SystemExit(1)

if newest:
    with open(MARK_FILE, 'w') as mark_file:
        mark_file.write(newest)

print(f'\n{reported} changed of {swept} swept. '
      f'Remember to ignore the mark now and then: --all.')
