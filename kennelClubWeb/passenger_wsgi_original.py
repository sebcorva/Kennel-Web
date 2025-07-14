import os
import sys

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.dirname(__file__))

# Configurar la variable de entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings_production')

# Importar la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application

# Aplicación Django
application = get_wsgi_application() 