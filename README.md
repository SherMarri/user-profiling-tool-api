# User Profiling Tool API

## Installation
1. Install [virtualenv](https://virtualenv.pypa.io/en/latest/index.html)
2. Set a new environment:
```
virtualenv venv
```
3. Activate environment:
```
source ./venv/bin/activate
```
4. Clone this repo

## Development
1. Activate virtualenv:
```
source ./venv/bin/activate
```
2. Access the repo folder:
```
cd ./user-profiling-tool-api
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Install Serverless Python Requirements plugin:
```
npm install
```

## How to run the cli script
`src.cli` package executes the script used for sending a task to the queue.

**Usage**:
```
python -m src.cli <s3_key> <email> <from_date> <to_date>
```
**Example**:
```
python -m src.cli my_dataset labs@citibeats.net 2020-08-01 2020-08-09
```

## Setting environment variables
1. Create **.env** file in **user-profiling-tool-api/src** directory.
2. Usage .env.example as a reference.
3. To add a new variable, follow this pattern:
```
VARIABLE_NAME="VARIABLE_VALUE"
```
4. Importing **settings.py** automatically loads the variables defined in **.env** file.

## Running unit tests
1. All unit tests should be placed in tests directory/package in any module.
2. The following command will auto-discover all unit tests and execute them.
```
python -m unittest
```
