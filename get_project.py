"""Retrieves a Project and all Tracklogs in that Project.

It is saved as a json in the 'projects' folder

The script does not download any images.
"""

import os
import json
import utils
import argparse
import swagger_client
from swagger_client.rest import ApiException

#Parses command line arguments
parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-p', '--project', dest='project_id', help='ProjectId for the project to retrieve.', required=True)
parser.add_argument('-r', '--readable', dest='human_readable', help='If the result should be human readable. Default is condensed json', action=argparse.BooleanOptionalAction)
args = parser.parse_args()

project_id = args.project_id
human_readable = args.human_readable

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
projects_api = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
tracklogs_api = swagger_client.TracklogsApi(swagger_client.ApiClient(configuration))

result = {}

#Get and write project
try:
    project = projects_api.get_project(project_id=project_id)
    result['id'] = project.id
    result['name'] = project.name
    result['team_id'] = project.team_id
    result['created'] = project.created
    result['updated'] = project.updated
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)

#Get and write tracklogs
try:
    tracklogs_response = tracklogs_api.get_tracklogs(project_id=project_id)
    tracklogs_list = list()
    for tracklog in tracklogs_response.results:
        tracklogs_list.append({
            'id' : tracklog.id,
            'name' : tracklog.name,
            'comment' : tracklog.comment,
            'created' : tracklog.created,
            'updated' : tracklog.updated,
            'geometry' : {'type' : tracklog.geometry.type,
                          'coordinates' : tracklog.geometry.coordinates},
            'geometry_last_changed' : tracklog.geometry_last_changed
            })
    result['tracklogs'] = tracklogs_list
except ApiException as e:
    print("Exception when calling TracklogsApi->get_tracklogs: %s\n" % e)

#Make sure folder exists
if not os.path.exists('projects'):
    os.makedirs('projects')

#Write result to file
with open('projects/Project_'+project.name+'.json', 'w') as output:
    if human_readable:
        json.dump(result, output, indent=4)
    else:
        json.dump(result, output)
