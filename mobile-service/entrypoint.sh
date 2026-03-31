#!/bin/bash
set -e

echo "Waiting for database..."
sleep 5

echo "Running migrations..."
python manage.py makemigrations mobile_app
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
