"""
Configuración ASGI para el proyecto proyecto1_django.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto1_django.settings')

application = get_asgi_application()
