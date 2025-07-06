#!/usr/bin/env python3
"""
Archivo de entrada para Django en cPanel
"""
import os
import sys

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configurar variables de entorno para producci贸n
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings_production')

# Importar y configurar Django
import django
django.setup()

# Importar la aplicaci贸n WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Para desarrollo local (opcional)
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv) 