#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py loaddata journal_entries/languages.json
python manage.py loaddata journal_entries/frameworks.json
echo "Starting server"
python manage.py runserver 0.0.0.0:8000