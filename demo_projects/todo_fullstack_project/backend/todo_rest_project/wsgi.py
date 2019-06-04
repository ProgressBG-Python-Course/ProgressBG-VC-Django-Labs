"""
WSGI config for todo_rest_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_rest_project.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "{{ todo_rest_project }}.settings"

application = get_wsgi_application()


# old versions
# os.environ['DJANGO_SETTINGS_MODULE'] = '<my-project-name>.settings'

# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()
