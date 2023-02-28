# App back-end

API to provide and receive data from a psychology app

This code is formatted using Black and tested with pytest

## Optional dependencies

- **Linux** - Add `127.0.0.1 psico.local` to `/etc/hosts` file to access the API using `api.local:8000/api`
- **Windows** - Add `127.0.0.1 psico.local` to `C:\Windows\System32\Drivers\etc\hosts` file to access the API using `api.local:8000/api`

## How to build

`docker-compose build`

## How to run

`docker-compose up -d`

## Seed database

Run inside the API container:

`python manage.py seed`

## Run tests

Run inside the API container:

`pytest`
