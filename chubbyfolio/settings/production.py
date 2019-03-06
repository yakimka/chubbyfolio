from .base import *

INSTALLED_APPS += ['gunicorn']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
