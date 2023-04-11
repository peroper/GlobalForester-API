# Global Forester API Example Scripts

This repository contains a collection of Python scripts intended as a starting point for developers looking to utilize the Global Forester API using Python and Swagger. These scripts can be used or combined as-is, or serve as inspiration for more complex implementations. To set up and run the scripts, follow the steps below.

See <https://api.globalforester.com/swagger> for more detailed information about the API.

The examples uses [version 3](https://api.globalforester.com/swagger/index.html?urls.primaryName=V3) of the API, which is the recommended version.

Examples for [version 2](https://api.globalforester.com/swagger/index.html?urls.primaryName=V2) of the API can be found [here](https://github.com/peroper/GlobalForester-API/tree/2.0). Note that version 2 only supports fetching data. Version 1 of the API has ceased to be and is now history.

## Getting Started

### 1. Clone the repo

```shell
git clone https://github.com/peroper/GlobalForester-API.git
cd GlobalForester-API
```

### 2. Install Python 3

<https://www.python.org>

### 3. Install Python Dependencies

It is recommended to install dependencies in a virtual environment. This will isolate project dependencies from other projects on the same computer. If you want to read more about virtual environments you can do so here: <https://docs.python.org/3/library/venv.html>

1. Create a virtual environment

   ```shell
   python3 -m venv venv
   ```

2. Activate the virtual environment

   ```shell
   source venv/bin/activate
   ```

3. Install dependencies

   ```shell
   pip3 install -r requirements.txt
   ```

### 4. Install swagger-codegen 3

Via Homebrew:

```shell
brew install swagger-codegen
```

For other installation methods, see: <https://github.com/swagger-api/swagger-codegen/tree/3.0.0>

### 5. Generate the API Client

```shell
swagger-codegen generate -i https://api.globalforester.com/swagger/v3/swagger.json -o Swagger -l python
```

> Scripts assume that the API Client is located in a folder called 'Swagger'

### 6. Run Scripts

1. Enter your client ID and client secret in _utils.py_. [Contact support](https://www.globalforester.com/manual/basics#errors-and-support) if you don't have a client ID and client secret and API access is included in your Global Forester subscription.
2. Run any desired script with:

   ```shell
   python3 name_of_script.py
   ```

3. To get more information about a script, run:

   ```shell
   python3 name_of_script.py -h
   ```
