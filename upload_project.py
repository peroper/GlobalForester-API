import json
import utils
import argparse
import swagger_client
from swagger_client.rest import ApiException

#Parses command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', dest='path', help='Relative path to the json containing the project details.')
parser.add_argument('-t', '--teamId', dest='team_id', help='Id of team to upload project to.')
args = parser.parse_args()

path = args.path
team_id = args.team_id

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
projects_api = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
observations_api = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
tracklogs_api = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))

project_file = open(path, 'r')
project = json.load(project_file)

try:
    request_object = swagger_client.GlobalForesterApiV1ControllersProjectsPostProjectRequestProject(project['name'])
    posted_project = projects_api.post_project(team_id, body = request_object)

    for observation in project['observations']:
        request_object = swagger_client.GlobalForesterApiV1ControllersObservationsPostObservationRequestObservation(
            name = observation['name'],
            comment = observation['comment'],
            geometry = {'type' : observation['geometry']['type'],
                        'coordinates' : observation['geometry']['coordinates']})
        try:
            observations_api.post_observation(posted_project.id, body = request_object)
        except ApiException as e:
            print(f"For observation {observation['name']}, {observation['id']}. Exception when calling ObservationsApi->post_observations: %s\n" % e)

    for tracklog in project['tracklogs']:
        request_object = swagger_client.GlobalForesterApiV1ControllersTracklogsPostTracklogRequestTracklog(
            name = tracklog['name'],
            comment = tracklog['comment'],
            geometry = {'type' : tracklog['geometry']['type'],
                        'coordinates' : tracklog['geometry']['coordinates']})
        try:
            tracklogs_api.post_tracklog(posted_project.id, body = request_object)
        except ApiException as e:
            print(f"For tracklog {tracklog['name']}, {tracklog['id']}. Exception when calling TracklogsApi->post_tracklog: %s\n" % e)

except ApiException as e:
    print("Exception when calling ProjectsApi->post_project: %s\n" % e)
