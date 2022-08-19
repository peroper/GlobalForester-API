import utils
import argparse
import swagger_client
from swagger_client.rest import ApiException

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--team', dest='team', help='Name of team to get projects from.')
parser.add_argument('-f', '--file', dest='file', help='If the result should be saved to file.', action=argparse.BooleanOptionalAction)
args = parser.parse_args()

team_name = args.team
save_to_file = args.file
filename = team_name + '_projects.txt'

configuration = utils.configure_swagger_client()
teams_api = swagger_client.TeamsApi(swagger_client.ApiClient(configuration))

try:
    teams = teams_api.get_teams()
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

project_api = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))

try:
    projects = project_api.get_projects(team.id)

    result = f'Team: {team_name}'
    for p in projects:
        result += f'\nName: {p.name},  Id: {p.id},  Created: {p.created}'

    print(result)

    if save_to_file:
        file = open(filename, 'w')
        file.write(result)
        file.close()

except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
