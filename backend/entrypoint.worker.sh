#!/bin/sh
# Using a different entrypoint for the worker so we don't
# create a race condition with the migrations that we run on the backend container
# which created duplicated data migrations

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL responding"
fi

exec "$@"
