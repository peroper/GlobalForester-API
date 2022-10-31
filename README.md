# Global Forester API Example Scripts

This repository contains a collection of Python scripts intended as a starting point for developers looking to utilize the Global Forester API using Python and Swagger. These scripts can be used or combined as-is, or serve as inspiration for more complex implementations. To set up and run the scripts, follow the steps below.

See https://api.globalforester.com/swagger for more detailed information about the API.

## Getting Started

### 1. Clone the repo
```shell
git clone https://github.com/peroper/GlobalForester-API.git
cd GlobalForester-API
```

### 2. Install Python 3
https://www.python.org

### 3. Install Python Dependencies

It is recommended to install dependencies in a virtual environment. This will isolate project dependencies from other projects on the same computer. If you want to read more about virtual environments you can do so here: https://docs.python.org/3/library/venv.html

* Create a virtual environment
```shell
python3 -m venv venv
```

* Activate the virtual environment
```shell
source venv/bin/activate
```

* Install dependencies
```shell
pip3 install -r requirements.txt
```

### 4. Install swagger-codegen 3
Via Homebrew:
```shell
brew install swagger-codegen
```
For other installation methods, see: https://github.com/swagger-api/swagger-codegen/tree/3.0.0

### 5. Generate the API Client

```shell
swagger-codegen generate -i https://api.globalforester.com/swagger/v1/swagger.json -o Swagger -l python
```

> Scripts assume that the API Client is located in a folder called 'Swagger'

### 6. Run Scripts

* Enter your client ID and client secret in _utils.py_. Contact support if you don't have a client ID and client secret and API access is included in your Global Forester subscription. https://www.globalforester.com/manual#errors-and-support
* Run any desired script with
```shell
 python3 name_of_script.py
 ```

 Available scripts:

- [get_projects_by_team.py](#get_projects_by_team)
- [get_observation.py](#get_observation)
- [post_observation.py](#post_observation)
- [download_projects](#download_projects)
- [upload_projects](#upload_projects)
- [get_rapid_orthophotos_for_project](#get_rapid_orthophotos_for_project)

> Most scripts also have arguments that need to be passed to them. These can be a value or a flag that is set to true if used. Running a script with only the -h or --help flag will show the options available.

## Scripts

### get_projects_by_team

get_projects_by_team is used to get all Projects in a Team, along with IDs for each project. These IDs are used in most other scripts.

#### Flags

- -t or --team, the name of the Team you want to get Projects from.
- -f or --file, use if you want the results to be saved to a file in the _/teams_ subfolder.

### get_observation

Downloads an Observation as a shapefile in the _/shapefiles_ subfolder. A shapefile is actually multiple files with the same name but different file endings. The script creates the following files:

- .dbf, contains the Observation data (such as comments).
- .shp, contains the Observation geometry.
- .prj, contains the reference with which to read the geometry coordinates.
- .shx, a register making reading the other files quicker.

If the Observation contains images they will be placed as jpeg files in a subfolder with the same name as the Observation.

#### Flags

- -p or --project, the ID of the Project that contains the Observation.
- -n or --name, the name of the Observation.

### post_observation

Uploads a shapefile as an Observation to an existing Project.

#### Flags

- -p or --project, the ID of the Project that contains the Observation.
- -f or --filepath, the relative path to the shapefile.

> If the shapefile is located in the default location for downloaded Observations the path would look like this: _shapefiles/observation_name_

### download_projects

Downloads a Project and all Observations and Tracklogs in that Project, and compiles it to a json. The script does not download any images.

#### Flags

- -p or --project, the ID of the Project.
- -t or --teamId, the ID of the Team the Project is in.
- -r or --readable, use if you want the resulting json in a human-readable format.

### upload_projects

Creates new Projects complete with Observations and Tracklogs from a json. The json must contain the following variables:
| Variable name | Type |
| ----------- | ----------- |
| name | String |
| observations | List |
| tracklogs | List |

The Observations and Tracklogs lists can be empty. An example Project can be found in the _/projects_ subfolder.

#### Flags

- -p or --path, the relative path to the json containing the Project details.
- -t or --teamId, the ID of the Team you want to upload your Projects to.

### get_rapid_orthophotos_for_project

Downloads all Rapid Orthophotos in a Project. The images are saved as jpeg files in the _/rapid_orthophotos_ subfolder.

#### Flags

- -p or --project, the ID of the Project that contains the Rapid Orthophotos.
