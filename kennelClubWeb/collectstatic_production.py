#!/usr/bin/env python3
"""
Script para ejecutar collectstatic en producción
"""
import os
import sys
import django
from pathlib import Path

# Agregar el directorio del proyecto al path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Configurar Django para producción
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings_production')

# Configurar Django
django.setup()

# Importar el comando collectstatic
from django.core.management import call_command
from django.conf import settings

def main():
    print("🚀 Ejecutando collectstatic para producción...")
    print(f"📁 STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"📁 STATIC_URL: {settings.STATIC_URL}")
    print(f"📁 STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    
    try:
        # Ejecutar collectstatic
        call_command('collectstatic', '--noinput', '--clear')
        print("✅ collectstatic ejecutado correctamente")
        
        # Verificar que los archivos se copiaron
        if os.path.exists(settings.STATIC_ROOT):
            print(f"✅ Directorio STATIC_ROOT existe: {settings.STATIC_ROOT}")
            
            # Listar archivos en staticfiles
            for root, dirs, files in os.walk(settings.STATIC_ROOT):
                level = root.replace(settings.STATIC_ROOT, '').count(os.sep)
                indent = ' ' * 2 * level
                print(f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 2 * (level + 1)
                for file in files:
                    print(f"{subindent}{file}")
        else:
            print(f"❌ ERROR: No se pudo crear el directorio STATIC_ROOT: {settings.STATIC_ROOT}")
            
    except Exception as e:
        print(f"❌ ERROR al ejecutar collectstatic: {e}")
        return False
    
    return True

if __name__ == '__main__':
    success = main()
    if success:
        print("\n🎉 ¡collectstatic completado exitosamente!")
        print("📋 Ahora sube todos los archivos a tu servidor")
    else:
        print("\n💥 Error al ejecutar collectstatic")
        sys.exit(1) 