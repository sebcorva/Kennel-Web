#!/bin/bash

# Script para ejecutar collectstatic automáticamente
# Este script debe ejecutarse como cron job

# Configurar variables de entorno
export DJANGO_SETTINGS_MODULE=kennelClubWeb.settings_production

# Ir al directorio del proyecto
cd /home/username/public_html/kennelClubWeb

# Activar el entorno virtual (si existe)
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

# Ejecutar collectstatic
python manage.py collectstatic --noinput

# Crear carpetas si no existen
mkdir -p staticfiles/uploads/noticias
mkdir -p staticfiles/uploads/jueces
mkdir -p staticfiles/uploads/clubes
mkdir -p staticfiles/uploads/historia_razas
mkdir -p staticfiles/uploads/tramites
mkdir -p staticfiles/uploads/curriculums
mkdir -p staticfiles/uploads/rankings
mkdir -p staticfiles/uploads/reglamentos

# Log de la ejecución
echo "$(date): collectstatic ejecutado automáticamente" >> /home/username/public_html/kennelClubWeb/cron.log

# Limpiar logs antiguos (mantener solo los últimos 30 días)
find /home/username/public_html/kennelClubWeb/cron.log -mtime +30 -delete 2>/dev/null 