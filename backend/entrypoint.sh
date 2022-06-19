#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrations
python manage.py migrate

# Create super user
python manage.py shell -c "$(cat <<-END
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
try:
  User = get_user_model()
  User.objects.create_superuser('admin', 'admin@example.com', 'password')
except IntegrityError:
  pass
END
)"

echo "Migrations complete"

exec "$@"
