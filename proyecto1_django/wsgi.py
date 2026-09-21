"""
Configuración WSGI para el proyecto proyecto1_django.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto1_django.settings')

application = get_wsgi_application()
