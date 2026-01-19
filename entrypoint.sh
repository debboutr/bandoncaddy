#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn -b :5000 core.wsgi
