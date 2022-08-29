import os
import utils
import shapefile
import swagger_client
from swagger_client.rest import ApiException
from argparse import ArgumentParser

#Parses command line arguments
parser = ArgumentParser()
parser.add_argument('-p', '--project', dest='project_id', help='ProjectId for the project that contains the observation.')
parser.add_argument('-n', '--name', dest='observation_name', help='Name of the observation.')
args = parser.parse_args()

project_id = args.project_id
observation_name = args.observation_name

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
observations_api = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
observation_files_api = swagger_client.ObservationFilesApi(swagger_client.ApiClient(configuration))

try:
    #Sends request
    observations = observations_api.get_observations(project_id)

    #Finds the correct observation by name
    observation = ''
    for o in observations:
        if o.name == observation_name:
            observation = o
            break
    if observation == '':
        print('Could not find observation')
        exit()
except ApiException as e:
    print("Exception when calling ObservationsApi->get_observations: %s\n" % e)

#Starts a writer for the shapefile.
shapefile_writer = shapefile.Writer(f'shapefiles/{observation_name}')
image_folder = ''

#Adds the geometry to the shapefile
if observation.geometry['type']== 'Point':
    shapefile_writer.shapeType = 1
    #The writer takes seperate x and y coordinates, the api gives both in a list
    shapefile_writer.point(observation.geometry['coordinates'][0],
                           observation.geometry['coordinates'][1])

    #Save images if there are any
    try:
        #Get list of files for observation
        observation_files = observation_files_api.get_observation_files(observation.id)

        if len(observation_files) > 0:
            image_folder = f'shapefiles/{observation_name}'
            if not os.path.exists(image_folder):
                os.makedirs(image_folder)

            for i, image_file in enumerate(observation_files):
                try:
                    #Get image
                    image_string = observation_files_api.get_image(observation.id, image_file.id)
                    image = eval(image_string)
                    #Writes the image to file
                    with open(image_folder+f'/{i}.jpeg', 'wb') as outfile:
                        outfile.write(image)

                except ApiException as e:
                    print("Exception when calling ObservationsFilesApi->get_image: %s\n" % e)

    except ApiException as e:
        print("Exception when calling ObservationsFilesApi->get_observations_files: %s\n" % e)

elif observation.geometry['type'] == 'LineString':
    shapefile_writer.shapeType = 3
    #The writer takes a nested list of coordinate lists. ex [[[x1,y1], [x2, y2]]]
    #The api gives the coordinates without the outer list so it has to be added.
    coordinate_list = list()
    coordinate_list.append(observation.geometry['coordinates'])
    shapefile_writer.line(coordinate_list)
elif observation.geometry['type'] == 'Polygon':
    shapefile_writer.shapeType = 5
    #The writer takes and the api gives a nested list of coordinate lists. ex [[[x1,y1], [x2, y2]]]
    shapefile_writer.poly(observation.geometry['coordinates'])

#Adds the fields the shapefile will have. First argument is the fields name, second is the type (C = string).
shapefile_writer.field('id', 'C')
shapefile_writer.field('projectId', 'C')
shapefile_writer.field('name', 'C')
shapefile_writer.field('comment', 'C')
shapefile_writer.field('geometryLstChanged', 'C')
shapefile_writer.field('created', 'C')
shapefile_writer.field('updated', 'C')
shapefile_writer.field('image_folder', 'C')

#This fills in the information in the first and in this case only record
shapefile_writer.record(
    id=observation.id,
    projectId=observation.project_id,
    name=observation.name,
    comment=observation.comment,
    geometryLstChanged=observation.geometry_last_changed,
    created=observation.created,
    updated=observation.updated,
    image_folder=image_folder
)

shapefile_writer.close()

#This creates a projection file for the shapefile.
#It is used to make sure the coordinates are read with the correct reference.
with open(f'shapefiles/{observation.name}.prj', 'w') as prj:
    prj.write('''GEOGCS["WGS 84",
              DATUM["WGS_1984", SPHEROID["WGS 84",6378137,298.257223563]],
              PRIMEM["Greenwich",0],
              UNIT["degree",0.0174532925199433,
                   AUTHORITY["EPSG","9122"]],
                   AUTHORITY["EPSG","4326"]]''')
