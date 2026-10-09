# books api
a simple api for managing books built with fastapi.

## requirements
- python >=3.12
- uv
- fastapi

## setup
after you made sure that you have uv and python intalled, simply run `uv run fastapi dev` for development mode and `uv run fastapi run` for production. it will install all the dependencies and starts the project. before that, make sure you are running `uv` with the correct version of python.

## project overview
this project uses simple variables for storing books which means, all data is earased when the script is restarted.
<br/>
pydantic is used for structing data and api models. see models.py.