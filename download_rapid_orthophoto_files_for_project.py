"""Downloads all Rapid Orthophoto files in a Project.

For each Rapid Orthophoto two files are downloaded:
- Originals: A zip file with the original images
- GeoPackage: A Geopackage with the map tiles

The downloaded files are stored in 'rapid_orthophotos'-folder
"""

import os
import utils
import swagger_client
from swagger_client.rest import ApiException
import argparse

#Parses command line arguments
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='ProjectId for the project that you want to download rapid orthophotos from.', required=True)
args = parser.parse_args()

project_id = args.project_id

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
rapid_orthophotos_api = swagger_client.RapidOrthophotosApi(swagger_client.ApiClient(configuration))
files_api = swagger_client.FilesApi(swagger_client.ApiClient(configuration))

try:
    #Get list of rapid orthophotos on project
    orthophoto_list_response = rapid_orthophotos_api.get_rapid_orthophotos(project_id=project_id)

    #Make sure folder exists
    if not os.path.exists('rapid_orthophotos'):
        os.makedirs('rapid_orthophotos')
except ApiException as e:
    print("Exception when calling RapidOrthophotosApi->get_rapid_orthophotos: %s\n" % e)

for orthophoto in orthophoto_list_response.results:
    print("Downloading files for orthophoto:", orthophoto.name)
    try:
        #Get links to geopackage and originals
        orthophoto_files = files_api.get_files(rapid_orthophoto_id=orthophoto.id)

        #orthophoto_files contains two dictionaries. One for the originals and one for the geopackage.
        #These are stored in a list in an arbitrary order.
        for file in orthophoto_files:
            if file.type == 'geoPackage':
                response=None
                try:
                    response = files_api.get_file(id=file.id, _preload_content=False)

                    #Writes the geopackage to file in chunks
                    with open(f'rapid_orthophotos/{orthophoto.name}_{orthophoto.id}.gpkg', 'wb') as outfile:
                      for chunk in response.stream(65536):
                        outfile.write(chunk)

                except Exception as e:
                    print(f"For rapid orthophoto {orthophoto.name}, {orthophoto.id}. Exception when downloading orthophoto: %s\n" % e)
                finally:
                    if (response != None):
                      try:
                        response.drain_conn()
                        response.release_conn()
                      except:
                        pass
            elif file.type == 'originals':
                response=None
                try:
                    response = files_api.get_file(id=file.id, _preload_content=False)

                    #Writes the originals to file in chunks
                    with open(f'rapid_orthophotos/{orthophoto.name}_{orthophoto.id}.zip', 'wb') as outfile:
                      for chunk in response.stream(65536):
                        outfile.write(chunk)

                except Exception as e:
                    print(f"For rapid orthophoto {orthophoto.name}, {orthophoto.id}. Exception when downloading originals: %s\n" % e)
                finally:
                  if (response != None):
                    try:
                      response.drain_conn()
                      response.release_conn()
                    except:
                      pass
            else:
                print(f'Encountered unexpected file type: {file.type}, when processing rapid orthophoto {orthophoto.name}, {orthophoto.id}.')
    except ApiException as e:
        print(f"For rapid orthophotos {orthophoto.name}, {orthophoto.id}. Exception when calling RapidOrthophotoFilesApi->get_rapid_orthophoto_files: %s\n" % e)
