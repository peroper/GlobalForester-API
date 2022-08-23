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

print(observation)

#Starts a writer for the shapefile.
shapefile_writer = shapefile.Writer('shapefiles/'+observation_name)

#Adds the geometry to the shapefile
if observation.geometry['type']== 'Point':
    shapefile_writer.shapeType = 1
    #The writer takes seperate x and y coordinates, the api gives both in a list
    shapefile_writer.point(observation.geometry['coordinates'][0],
                           observation.geometry['coordinates'][1])
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

#This fills in the information in the first and in this case only record
shapefile_writer.record(
    id=observation.id,
    projectId=observation.project_id,
    name=observation.name,
    comment=observation.comment,
    geometryLstChanged=observation.geometry_last_changed,
    created=observation.created,
    updated=observation.updated
)

shapefile_writer.close()
