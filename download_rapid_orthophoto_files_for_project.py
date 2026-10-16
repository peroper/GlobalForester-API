"""Downloads all Rapid Orthophoto files in a Project.

For each Rapid Orthophoto two files are downloaded:
- originals: a zip with the original images
- geoPackage: a GeoPackage with the map tiles

The downloaded files are stored in the 'rapid_orthophotos' folder, written in chunks so a large file
is never held in memory.
"""

import argparse

import utils

EXTENSIONS = {'geoPackage': 'gpkg', 'originals': 'zip'}

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='Id of the Project to download Rapid Orthophotos from.', required=True)
args = parser.parse_args()

api = utils.client()

try:
    orthophotos = [o for o in api.items('/v4/rapidOrthophotos', {'projectId': args.project_id})
                   if not o.get('deleted')]
except utils.ApiError as error:
    print(f'Could not list orthophotos: {error.code} - {error.detail}')
    raise SystemExit(1)

for orthophoto in orthophotos:
    print(f"Downloading files for orthophoto: {orthophoto.get('name')}")

    for file in api.items('/v4/files', {'rapidOrthophotoId': orthophoto['id']}):
        if file.get('deleted'):
            continue

        extension = EXTENSIONS.get(file.get('type'))
        if extension is None:
            print(f"  unexpected file type {file.get('type')} on {file['id']}, skipped")
            continue

        try:
            written = api.download(
                f"/v4/files/{file['id']}",
                f"rapid_orthophotos/{orthophoto.get('name')}_{orthophoto['id']}.{extension}")
            print(f'  saved {written}')
        except utils.ApiError as error:
            print(f"  could not download {file['id']}: {error.code} - {error.detail}")
