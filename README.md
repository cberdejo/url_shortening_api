[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Project Title:  URL SHORTENING API
Using an api you could submit an url and recieve a shortened response



## Setup
### 1. Install Dependencies:

Ensure Python is installed.


### 2. Install required packages:

``` sh 
$ pip install -r requirements.txt
```
and for developing (tests and contributing), execute
``` sh 
$ pip install -r requirements-dev.txt
```

### 3. Environment Variables:


Create a `.env` file based on the `env.template` file provided in the project.


#### Define the following variables:

- DB_USER=<your_db_user>
- DB_PASSWORD=<your_db_password>
- DB_HOSTNAME=<your_db_hostname>
- DB_SID=<your_db_sid>
- DB_PORT=<your_port>

### Redis

### Image PostreSQL 
Postre:
``` sh 
    $ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=departements -p 5432:5432 postgres

```

## Execute the script:
Use 
``` sh 
python 
```


## LICENSE: MIT License file.
License
This project is licensed under the MIT License. See the LICENSE file for details.