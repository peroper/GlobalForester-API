"""Uploads a shapefile as an Observation to an existing Project"""

import utils
import shapefile
import swagger_client
from swagger_client.rest import ApiException
import argparse

#Parses command line arguments
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='ProjectId for the project that you want to upload the observation to.', required=True)
parser.add_argument('-f', '--filepath', dest='file_path', help='Path to the shapefile. If the shapefile is located in the default location for downloaded Observations the path would look like this: "shapefiles/observation_name"', required=True)
args = parser.parse_args()

project_id = args.project_id
file_path = args.file_path

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
observations_api = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))

#Starts shapefile reader
shapefile_reader = shapefile.Reader(file_path)

#Formats the geometry and geometrytype
shape_type = ''
coordinates = list()
if shapefile_reader.shapeType == 1:
    shape_type = 'Point'
    #The swagger does not accept arrays. The coordinates are therefore put in a tuple
    coordinates = tuple(shapefile_reader.shape(0).points[0])
elif shapefile_reader.shapeType == 3:
    shape_type = 'LineString'
    #Lines are lists of coordinate tuples
    for point in shapefile_reader.shape(0).points:
        coordinates.append(tuple(point))
elif shapefile_reader.shapeType == 5:
    shape_type = 'Polygon'
    #Polygons have two layers of lists. The first and last point are always the same.
    coordinates_inner = list()
    for point in shapefile_reader.shape(0).points:
        coordinates_inner.append(tuple(point))
    coordinates.append(coordinates_inner)

#Creates the object that serves as the request body
request_object = swagger_client.GlobalForesterApiV2ControllersObservationsPostObservationRequestObservation(
    project_id = project_id,
    name = shapefile_reader.record(0).name,
    comment = shapefile_reader.record(0).comment,
    geometry = {'type' : shape_type,
                'coordinates' : coordinates})

try:
    #Sends request
    observations = observations_api.post_observation(body = request_object)

except ApiException as e:
    print("Exception when calling ObservationsApi->post_observations: %s\n" % e)
