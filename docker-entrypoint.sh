#!/usr/bin/env bash



python3 manage.py makemigrations
python3 manage.py migrate

gunicorn --bind 0.0.0.0:80 blog.wsgi:application



