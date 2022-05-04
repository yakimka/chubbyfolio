#!/bin/bash

python collectfrontend.py
python manage.py collectstatic --no-input
python manage.py migrate
gunicorn chubbyfolio.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/app
