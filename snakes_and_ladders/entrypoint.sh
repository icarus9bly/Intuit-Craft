#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

gunicorn --bind :8044 snakes_and_ladders.wsgi:application
#gunicorn --bind :8044 snakes_and_ladders.wsgi:application --reload --daemon