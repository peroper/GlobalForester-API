## Generate swagger 
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

## Running the scripts
Before running the scripts client ID and client secret needs to be given. The variables are found in utils.py.

Python scripts are run with: python *name_of_script.py*

Most scripts also have arguments that need to be passed to them. These can be a value or a flag that is set to true if used.

  ex `python get_projects_by_team -t TEAM_NAME -f`
  
Calling a script with only the flag -h or --help will show the options avaible.
