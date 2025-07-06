#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Archivo de configuracion para Django en cPanel con Passenger
"""
import os
import sys

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configurar variables de entorno para produccion
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings_production')

# Importar y configurar Django
import django
django.setup()

# Importar la aplicacion WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()