#!/bin/bash

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn chubbyfolio.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app
