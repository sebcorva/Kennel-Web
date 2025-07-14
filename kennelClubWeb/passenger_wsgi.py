import os
import sys

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.dirname(__file__))

# Configurar la variable de entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings_production')

# Importar la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
from django.conf import settings

# Obtener la aplicación Django
django_app = get_wsgi_application()

# Configurar WhiteNoise para archivos estáticos y media
if not settings.DEBUG:
    from whitenoise import WhiteNoise
    
    # Crear aplicación WhiteNoise que sirve archivos estáticos y media
    application = WhiteNoise(django_app)
    
    # Agregar archivos estáticos
    application.add_files(settings.STATIC_ROOT, prefix=settings.STATIC_URL.strip('/'))
    
    # Agregar archivos media - IMPORTANTE: usar el prefijo correcto
    application.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL.strip('/'))
    
    # Configuración adicional
    application.autorefresh = True
    application.max_age = 31536000  # 1 año
    
    print("WhiteNoise configurado para servir archivos media desde:", settings.MEDIA_ROOT)
    print("Prefijo usado para media:", settings.MEDIA_URL.strip('/'))
else:
    # En desarrollo, usar la aplicación Django normal
    application = django_app 