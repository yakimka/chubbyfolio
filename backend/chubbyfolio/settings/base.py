"""
Django settings for chubbyfolio project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# APPS_DIR = os.path.join(BASE_DIR, 'django_apps')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=lambda v: [d for d in [s.strip() for s in v.split(' ')] if d],
    default='',
)


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'dynamic_preferences',
    'rest_framework',
    'corsheaders',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'django_extensions'
]

LOCAL_APPS = [
    'photosets',
    'dynamic_settings',
    'feedback',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chubbyfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chubbyfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

##############################################################################

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

FILE_UPLOAD_PERMISSIONS = 0o644

REST_FRAMEWORK = {
    # Specify date format
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATETIME_INPUT_FORMATS': '%Y-%m-%d %H:%M:%S',
    'DATE_FORMAT': '%Y-%m-%d',
    'DATE_INPUT_FORMAT': '%Y-%m-%d',
    'TIME_FORMAT': '%H:%M:%S',
    'TIME_INPUT_FORMAT': '%H:%M:%S',
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 36,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '500/minute',
        'message': '20/hour',
    },
    'DEFAULT_AUTHENTICATION_CLASSES': []
}

CORS_ORIGIN_WHITELIST = config(
    'CORS_ORIGIN_WHITELIST',
    cast=lambda v: [d for d in [s.strip() for s in v.split(' ')] if d],
    default='',
)

PHOTOSET_PHOTO_WIDTH = 600
PHOTOSET_PHOTO_HEIGHT = 675
PHOTOSET_PHOTO_QUALITY = 90

THUMBNAIL_ALIASES = {
    '': {
        'home_slider': {'size': (480, 950), 'crop': 'smart', 'quality': 90},
        '500x500': {'size': (500, 500), 'crop': False, 'quality': 90},
        '1000x1000': {'size': (1000, 1000), 'crop': False, 'quality': 90},
        'p1': {'size': (460, 657), 'crop': 'smart', 'quality': 90},
        'p2': {'size': (558, 585), 'crop': 'smart', 'quality': 90},
        'p3': {'size': (967, 657), 'crop': 'smart', 'quality': 90},
        'p4': {'size': (560, 557), 'crop': 'smart', 'quality': 90},
        'p5': {'size': (460, 657), 'crop': 'smart', 'quality': 90},
        'p6': {'size': (326, 469), 'crop': 'smart', 'quality': 90},
        'p7': {'size': (360, 531), 'crop': 'smart', 'quality': 90},
    },
}

THUMBNAIL_OPTIMIZE_COMMAND = {
    'jpeg': '/usr/bin/jpegoptim {filename} --strip-all',
}
