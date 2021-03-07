#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"

    echo "Creating the database tables..."
    python run.py create_db
    echo "Tables created"
    python run.py seed_db
    echo "User admin created"
fi

exec "$@"