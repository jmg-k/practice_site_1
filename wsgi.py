import os

from django.core.wsgi import get_wsgi_application

server_env = 'production'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'practice_site_1.settings.production')

application = get_wsgi_application()
