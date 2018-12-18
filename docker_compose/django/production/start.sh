#!/bin/sh
python /app/manage.py collectstatic --noinput
python /app/manage.py migrate
/usr/local/bin/gunicorn chubbyfolio.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app