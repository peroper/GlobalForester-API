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

configuration = utils.configure_swagger_client()
observations_api = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))

try:
    #Creates an instance of the swagger api
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

#Starts a writer for the shapefile. Only the dbf file is written since we do not have the geometry
shape_file_writer = shapefile.Writer(dbf='shapefiles/'+observation_name+'.dbf')

#Adds the fields the shapefile will have. First argument is the fields name, second is the type (C = string).
shape_file_writer.field('id', 'C')
shape_file_writer.field('projectId', 'C')
shape_file_writer.field('name', 'C')
shape_file_writer.field('comment', 'C')
shape_file_writer.field('geometryLstChanged', 'C')
shape_file_writer.field('created', 'C')
shape_file_writer.field('updated', 'C')

#This fills in the information in the first and in this case only record
shape_file_writer.record(
    id=observation.id,
    projectId=observation.project_id,
    name=observation.name,
    comment=observation.comment,
    geometryLstChanged=observation.geometry_last_changed,
    created=observation.created,
    updated=observation.updated
)

shape_file_writer.close()
