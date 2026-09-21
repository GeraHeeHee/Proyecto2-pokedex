"""
Configuración de URLs del proyecto proyecto1_django.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokedex.urls')),
]
