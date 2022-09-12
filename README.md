# Global Forester Example Scripts
This project is a collection of scripts, that is to say it is not a single cohesive program. The scripts are a way to interface with the Global Forester API using python and swagger. The project is not meant to be viewed as a complete implementation but rather as inspiration and a jumping off point for other projects. Below how to set up and run the scripts will be explained.

## Generate Swagger 
The swagger can be generated with swagger-codegen. https://github.com/swagger-api/swagger-codegen/tree/3.0.0
The command is: swagger-codegen generate -i *input-spec, (file or web-adress)* -o *output directory* -l *language*

  ex. `swagger-codegen generate -i https://api.globalforester.com/swagger/v1/swagger.json -o Swagger -l python`
  
The scripts assume that the swagger is located in a folder called 'Swagger'.
  
If you use homebrew, swagger-codegen can be installed with: `brew install swagger-codegen`

Other methods of installation are detailed in the link above.

## Dependencies
The scripts are using python3 and should be used with python3. The dependancies can be installed with:
 
 `pip install -r requirements.txt`
 
It is recommended to install the dependancies in a virtual environment. 
This will isolate this project' dependencies from other projects on the same computer.
 
A virtual environment can be created using python -m venv */path/to/new/virtual/environment*
 
  ex `python -m venv venv`
  
The virtual environment is activated with: source */path/to/virtual/environment/bin/activate*
  
  ex. `source venv/bin/activate`
  
If you want to read more about virtual environments you can do so here: https://docs.python.org/3/library/venv.html

## Running the Scripts
Before running the scripts client ID and client secret needs to be given. The variables are found in utils.py.

Python scripts are run with: python *name_of_script.py*

Most scripts also have arguments that need to be passed to them. These can be a value or a flag that is set to true if used.

  ex `python get_projects_by_team -t TEAM_NAME -f`
  
Calling a script with only the flag -h or --help will show the options avaible.

## Scripts
Here a short explanation of each script will be given

### get_projects_by_team
#### Flags
-t, --team: This is the name team you want to get the projects from

-f, --file: This is a boolean. Add if you want the result to be saved to a file.

#### Purpose
This script is used to see what projects exist on a team and to see what Id:s they have. The Id:s are used by most other scripts. If the result is saved to a file the result can be found in the map called teams.

### get_observation
#### Flags
-p, --project: The Id for the project that contains the observation.

-n, --name: The name of the observation

#### Purpose
This script downloads a observation. The observation will be saved as a shapefile in the folder called shapefiles. A shapefile is actually multiple files with the same name but different file-endings. The ones created by the script are:  
* .dbf - contains the observations data ex. comments
* .shp - contains the observations geometry
* .prj - contains the reference with wich to read the geometrys coordinates
* .shx - this is a register making reading the other files quicker

If the observation contains images they will be placed as jpeg files i a subfolder with the same name as the observation.

### post_observation
#### Flags
-p, --project: The Id for the project that contains the observation.

-f, --filepath: The relative path to the shapefile. If the shapefile is located in the default location for download observations the path would look like this: "shapefiles/observation_name"

#### Purpose
With this script you can upload a shapefile as an observation to an existing project.

### get_rapid_orthophotos_for_project
#### Flags
-p, --project: The Id for the project that contains the rapid orthophotos.

#### Purpose
This script downloads all rapid orthophotos on a project. The images are saved as jpeg files under rapid_orthophotos/.
