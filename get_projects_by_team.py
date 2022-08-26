import utils
import argparse
import swagger_client
from swagger_client.rest import ApiException

#Parses command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--team', dest='team', help='Name of team to get projects from.')
parser.add_argument('-f', '--file', dest='file', help='If the result should be saved to file.', action=argparse.BooleanOptionalAction)
args = parser.parse_args()

team_name = args.team
save_to_file = args.file
filename = team_name + '_projects.txt'

#Creates an instance of the swagger api
configuration = utils.configure_swagger_client()
teams_api = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))
project_api = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))

#Get team
try:
    #Sends request
    teams = teams_api.get_teams()

    #Finds the correct team by name
    team = ''
    for t in teams:
        if t.name == team_name:
            team = t
            break
    if team == '':
        print('Could not find team')
        exit()
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams: %s\n" % e)

#Get projectId
try:
    #Sends request
    projects = project_api.get_projects(team.id)

    #Compile project information
    result = f'Team: {team_name}, Id: {team.id}'
    for p in projects:
        result += f'\nName: {p.name},  Id: {p.id},  Created: {p.created}'

    print(result)

    #Write to file
    if save_to_file:
        file = open(filename, 'w')
        file.write(result)
        file.close()

except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
