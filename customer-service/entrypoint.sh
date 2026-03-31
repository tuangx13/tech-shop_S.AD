#!/bin/bash
set -e

echo "Waiting for database..."
sleep 10

echo "Running migrations..."
python manage.py makemigrations customer_app --noinput
python manage.py migrate --noinput

echo "Starting customer service..."
python manage.py runserver 0.0.0.0:8000
