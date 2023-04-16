#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for postgres..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

if [ "$ENV" = "prod" ]
then
  echo "Collecting static files"

  python manage.py collectstatic
fi

echo "Migrating database"

# Run migrations
python manage.py migrate

echo "Migrations complete"

exec "$@"
