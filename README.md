[![Build Status](https://travis-ci.org/kmwangemi/Store-Manager-Challenge-3.svg?branch=develop)](https://travis-ci.org/kmwangemi/Store-Manager-Challenge-3) [![Coverage Status](https://coveralls.io/repos/github/kmwangemi/Store-Manager-Challenge-3/badge.svg?branch=develop)](https://coveralls.io/github/kmwangemi/Store-Manager-Challenge-3?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/23d069b21554c8e82c3f/maintainability)](https://codeclimate.com/github/kmwangemi/Store-Manager-Challenge-3/maintainability)

# Store-Manager-Challenge-3
An Application that helps store owners manage sales and product inventory records.

# Installation and Setup
Clone the repository.
```bash
git clone https://github.com/kmwangemi/Store-Manager-App.git
```
## Navigate to the app folder
```bash
cd Store-Manager-App/app
```

## Create a virtual environment

```bash
$ python3 -m venv venv;
$ source venv/bin/activate
```
On Windows
```bash
py -3 -m venv venv
```
If you need to install virtualenv because you are on an older version of Python:
```bash
virtualenv venv
```
On Windows
```bash
\Python27\Scripts\virtualenv.exe venv
```

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```bash
source venv/bin/activate
```
On Windows
```bash
venv\Scripts\activate
```

## Install requirements
```bash
$ pip install -r requirements.txt
```

## Running the application
After the configuration, you will run the app 
```bash
$ export FLASK_APP=run.py
$ flask run
```

## Endpoints
All endpoints can be now accessed from the following url on your local computer
```
http://localhost:5000/api/v1/
```

## Testing
After successfully installing the application, the endpoints can be tested by running.
```bash
nosetests app/tests/V1/*
```

Or with coverage
```bash
nosetests tests/V1/* --with-coverage --cover-package=app && coverage report
```
## Available endpoints
|  Endpoint  | Task  |
|  ---  | --- |
| `POST api/v1/users` | Admin can create users | 
| `GET api/v1/users/` | Admin can get all users |
| `GET api/v1/users/<userId>` | Admin can get a single user |
| `POST api/v1/products` | Admin can create products | 
| `GET api/v1/products/` | Admin can get all created products |
| `GET api/v1/products/<productId>` | Admin can get a single created product |
| `POST api/v1/sales` | User can create a sale | 
| `GET api/v1/sales` | Admin can get all sales |
| `GET api/v1/sales/<saleId>` | Admin can get a single sale |



