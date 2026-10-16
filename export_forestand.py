"""Exports an Område's plan as Forestand XML.

The plan comes back in the standard Forestand variant, whatever organisation is asking, so there is
no variant to choose. No Global Forester ids appear in the XML: the ids in it are running numbers,
and placeId is the external id.

An export is heavy, so only a few run at once. Beyond that the answer is 429 with Retry-After -
wait that many seconds and ask again. The helper does the waiting, and gives up after a few tries
rather than hanging forever; the message then says how long the server last asked for.

The file is written in chunks to the 'forestand' folder, so a whole plan is never held in memory.
"""

import argparse

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-m', '--managed-area', dest='managed_area_id', help='Id of the Område to export.', required=True)
parser.add_argument('-o', '--out', dest='out', help='Where to write the XML. Default is forestand/<managedAreaId>.xml')
args = parser.parse_args()

api = utils.client()

destination = args.out or f'forestand/{args.managed_area_id}.xml'

try:
    written = api.download(f'/v4/managedAreas/{args.managed_area_id}/forestand', destination)
except utils.ApiError as error:
    if error.code == 'tooManyConcurrentRequests':
        print(f'The server is still busy after several tries. '
              f'It last asked us to wait {error.retry_after}s. Try again later.')
    elif error.code == 'managedAreaNotFound':
        print(f'No managed area with that id is available to you. ({error.detail})')
    else:
        print(f'Could not export the plan: {error.code} - {error.detail}')
    raise SystemExit(1)

print(f'Wrote {written} ({written.stat().st_size} bytes).')
