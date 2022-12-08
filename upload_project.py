"""Creates a new Project from a json.

The json must contain the following properties:
- name: the name of the project
- observations: a list with observations (can be an empty list)
- tracklogs: a list with tracklogs (can be an empty list)

An example Project can be found in the 'projects' folder.
"""

import json
import utils
import argparse
import swagger_client
from swagger_client.rest import ApiException

#Parses command line arguments
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--path', dest='path', help='Relative path to the json containing the project details.', required=True)
parser.add_argument('-t', '--teamId', dest='team_id', help='Id of team to upload project to.', required=True)
args = parser.parse_args()

path = args.path
team_id = args.team_id

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
projects_api = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
observations_api = swagger_client.ObservationsApi(swagger_client.ApiClient(configuration))
tracklogs_api = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))

with open(path, 'r') as project_file :
    project = json.load(project_file)

    try:
        #Creates a new project on the specified team
        request_object = swagger_client.GlobalForesterApiV2ControllersProjectsPostProjectRequestProject(
          team_id = team_id,
          name = project['name'])
        posted_project = projects_api.post_project(body = request_object)

        #Creates observations from the json on the new project
        for observation in project['observations']:
            request_object = swagger_client.GlobalForesterApiV2ControllersObservationsPostObservationRequestObservation(
                project_id = posted_project.id,
                name = observation['name'],
                comment = observation['comment'],
                geometry = {'type' : observation['geometry']['type'],
                            'coordinates' : observation['geometry']['coordinates']})
            try:
                observations_api.post_observation(body = request_object)
            except ApiException as e:
                print(f"For observation {observation['name']}, {observation['id']}. Exception when calling ObservationsApi->post_observations: %s\n" % e)

        #Creates tracklogs from the json on the new project
        for tracklog in project['tracklogs']:
            request_object = swagger_client.GlobalForesterApiV2ControllersTracklogsPostTracklogRequestTracklog(
                project_id = posted_project.id,
                name = tracklog['name'],
                comment = tracklog['comment'],
                geometry = {'type' : tracklog['geometry']['type'],
                            'coordinates' : tracklog['geometry']['coordinates']})
            try:
                tracklogs_api.post_tracklog(body = request_object)
            except ApiException as e:
                print(f"For tracklog {tracklog['name']}, {tracklog['id']}. Exception when calling TracklogsApi->post_tracklog: %s\n" % e)

    except ApiException as e:
        print("Exception when calling ProjectsApi->post_project: %s\n" % e)
