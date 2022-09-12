import os
import utils
import swagger_client
from swagger_client.rest import ApiException
from argparse import ArgumentParser

#Parses command line arguments
parser = ArgumentParser()
parser.add_argument('-p', '--project', dest='project_id', help='ProjectId for the project that you want to download rapid orthophotos from.')
args = parser.parse_args()

project_id = args.project_id

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
rapid_orthophotos_api = swagger_client.RapidOrthophotosApi(swagger_client.ApiClient(configuration))
rapid_orthophoto_files_api = swagger_client.RapidOrthophotoFilesApi(swagger_client.ApiClient(configuration))

try:
    #Get list of rapid orthophotos on project
    orthophoto_list = rapid_orthophotos_api.get_rapid_orthophotos(project_id)

    #Make sure folder exists
    if not os.path.exists('rapid_orthophotos'):
        os.makedirs('rapid_orthophotos')
except ApiException as e:
    print("Exception when calling RapidOrthophotosApi->get_rapid_orthophotos: %s\n" % e)

for orthophoto in orthophoto_list:
    try:
        #Get links to geopackage and originals
        orthophoto_files = rapid_orthophoto_files_api.get_rapid_orthophoto_files(orthophoto.id)

        #orthophoto_files contains two dictionaries. One for the originals and one for the geopackage.
        #These are stored in a list in an arbitrary order.
        for file in orthophoto_files:
            if file.type == 'geoPackage':
                try:
                    #Get geopackage as a bytestring
                    geo_package_string = rapid_orthophoto_files_api.get_rapid_orthophoto_geo_package(orthophoto.id, file.id)
                    geo_package = eval(geo_package_string)

                    #Writes the geopackage to file
                    with open(f'rapid_orthophotos/{orthophoto.name}_{orthophoto.id}.gpkg', 'wb') as outfile:
                        outfile.write(geo_package)
                except ApiException as e:
                    print(f"For rapid orthophoto {orthophoto.name}, {orthophoto.id}. Exception when calling RapidOrthophotoFilesApi->get_rapid_orthophoto_geo_package: %s\n" % e)
            elif file.type == 'originals':
                print(file.type)
                try:
                    #Get originals as a bytestring
                    originals_string = rapid_orthophoto_files_api.get_rapid_orthophoto_originals(orthophoto.id, file.id)
                    originals = eval(originals_string)

                    #Writes the originals to file
                    with open(f'rapid_orthophotos/{orthophoto.name}_{orthophoto.id}.zip', 'wb') as outfile:
                        outfile.write(originals)
                except ApiException as e:
                    print(f"For rapid orthophoto {orthophoto.name}, {orthophoto.id}. Exception when calling RapidOrthophotoFilesApi->get_rapid_orthophoto_originals: %s\n" % e)
            else:
                print(f'Encountered unexpected file type: {file.type}, when processing rapid orthophoto {orthophoto.name}, {orthophoto.id}.')
    except ApiException as e:
        print(f"For rapid orthophotos {orthophoto.name}, {orthophoto.id}. Exception when calling RapidOrthophotoFilesApi->get_rapid_orthophoto_files: %s\n" % e)
