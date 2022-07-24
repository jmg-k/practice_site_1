import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['circus-records.co.uk', 'www.circus-records.co.uk']
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = ['https://circus-records.co.uk', ]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ['DB_HOST'],
#         'USER': os.environ['DB_USER'],
#         'PASSWORD': os.environ['DB_PASSWORD'],
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }
