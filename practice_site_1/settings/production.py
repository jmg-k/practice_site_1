import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['circus-records.co.uk', 'www.circus-records.co.uk']
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': 5432
    }
}
