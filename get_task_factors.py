"""Lists an Uppgift's Påverkansfaktorer and downloads their pictures.

This is where /v3/observations went. An observation is one of the types here (type: observation)
and nothing filters it out, so one call gives every Påverkansfaktor the field work left on the
Uppgift. type and subType are the app's own words rather than a value set V4 decides, so a kind
this script does not know can still turn up.

Pictures are downloaded to the 'factor_images' folder. A picture the app has not finished uploading
is left out of the list, because it cannot be downloaded yet.
"""

import argparse

import utils

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-t', '--task', dest='task_id', help='Id of the Uppgift to list Påverkansfaktorer for.', required=True)
parser.add_argument('-i', '--images', dest='download_images', help='Also download the pictures.', action='store_true')
parser.add_argument('-d', '--include-deleted', dest='include_deleted', help='Also list Påverkansfaktorer that have been deleted.', action='store_true')
args = parser.parse_args()

api = utils.client()

params = {'taskId': args.task_id}
if args.include_deleted:
    params['includeDeleted'] = 'true'

try:
    factors = list(api.items('/v4/factors', params))
except utils.ApiError as error:
    print(f'Could not list factors: {error.code} - {error.detail}')
    raise SystemExit(1)

try:
    for factor in factors:
        if factor.get('deleted'):
            print(f"{factor['id']}  (deleted)")
            continue

        geometry = factor.get('geometry') or {}
        print(f"{factor['id']}  type={factor.get('type')}  subType={factor.get('subType')}  "
              f"name={factor.get('name')}  geometry={geometry.get('type')}")
        if factor.get('note'):
            print(f"  note: {factor['note']}")

        pictures = list(api.items('/v4/files', {'factorId': factor['id']}))
        for picture in pictures:
            print(f"  picture {picture['id']} ({picture.get('type')})")

            if args.download_images:
                destination = api.download(
                    f"/v4/files/{picture['id']}",
                    f"factor_images/{factor['id']}_{picture['id']}.jpg")
                print(f'    saved to {destination}')
except utils.ApiError as error:
    print(f'Could not read the pictures: {error.code} - {error.detail}')
    raise SystemExit(1)

print(f'\n{len(factors)} factor(s) on task {args.task_id}.')
