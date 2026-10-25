# books api
a simple api for managing books built with fastapi.

## requirements
- python >=3.12
- uv
- postgres

## setup
- make sure you have postgres and uv installed and running.
- rename `.env.example` file to `.env`.
- for variable SQLALCHEMY_URL, change `user` to your database's user, `password` to your user's password, `host` to your postgres'es host address, `port` to it's port and `mydatabase` to name of the database you want to store data in.
- run command `uv run fastapi dev` to start in development mode and `uv run fastapi run` for production mode. it installs dependencies and runs the project.