#!/bin/bash
set -e

echo "Waiting for MySQL database..."
sleep 10

echo "Running migrations..."
python manage.py makemigrations authentication --noinput
python manage.py migrate --noinput

echo "Starting auth service..."
python manage.py runserver 0.0.0.0:8000
