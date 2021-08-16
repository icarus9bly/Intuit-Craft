#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

gunicorn --bind :8044 kamikaze3.wsgi:application
#gunicorn --bind :8044 kamikaze3.wsgi:application --reload --daemon