#!/bin/bash
set -e

echo "Starting SSH ..."
service ssh start

# python /code/manage.py runserver 0.0.0.0:8000

# gunicorn deeptech.wsgi:application --bind 0.0.0.0:$PORT
gunicorn deeptech.wsgi:application --bind 0.0.0.0:8888

