# App back-end

API to provide and receive data from a psychology app

This code is formatted using Black and tested with pytest

## Optional dependencies

To have a friendly url to access the API in the local environment, it's possible to create it using the following steps:

- **For Linux OS:** Add `127.0.0.1 psico.local` to `/etc/hosts` file to access the API using `psico.local:8000/api`
- **For Windows OS:** Add `127.0.0.1 psico.local` to `C:\Windows\System32\Drivers\etc\hosts` file to access the API using `psico.local:8000/api`

## How to build

`docker-compose build`

## How to run

`docker-compose up -d`

## Seed database

Seeding the database will populate the models `City`, `Profession`, `Plan` and will create an admin `Profile` with username `admin` and password `password`

Run inside the API container:

`python manage.py seed`

## Run tests

Run inside the API container:

`pytest`
