# App back-end

API and administration UI to provide and receive data from a psychology app

This code is formatted using Black and tested with pytest

## Optional dependencies

To have a friendly url to access the API in the local environment, it's possible to create it using the following steps:

- **For Linux OS:** Open `/etc/hosts` file
- **For Windows OS:** Open `C:\Windows\System32\Drivers\etc\hosts` file

Add `127.0.0.1 api.calendr admin.calendr` to the file file to access the API using `api.calendr:8000` and the administration UI using `admin.calendr:8000`

## How to build

`docker-compose build`

## How to run

`docker-compose up -d`

## Check logs

`docker-compose logs -f --tail 100 <docker service>`

Exemple: `docker-compose logs -f --tail 100 calendr_api` to see the API logs

## Seed database

The seeding process happens everytime the container is initiated.

Seeding the database will populate the models `City`, `Profession`, `Patient`, `Plan` and will create an admin `Profile` with the following data:

- username: `admin`
- email: `admin@example.com`
- password: `password`

In order to run the seed manually open the API container and run:

`./manage.py seed`

## Run tests

Run inside the API container:

`pytest`

## Swagger

Swagger is visble in the route `/swagger` -> `api.calendr:8000/swagger`

### How to create/update a Swagger schema

Run inside the API container:

`./manage.py spectacular --file schema.yml`
