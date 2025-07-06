#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar logs de debug personalizados
"""
import os
import sys
import traceback
from datetime import datetime

def log_error(message, error=None):
    """Registra un error en el archivo de log"""
    log_file = os.path.join(os.path.dirname(__file__), 'debug.log')
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")
        if error:
            f.write(f"Error: {str(error)}\n")
            f.write(f"Traceback: {traceback.format_exc()}\n")
        f.write("-" * 50 + "\n")

def check_django_setup():
    """Verifica la configuración de Django"""
    try:
        # Agregar el directorio del proyecto al path
        sys.path.insert(0, os.path.dirname(__file__))
        
        # Configurar Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings_production')
        
        import django
        django.setup()
        
        log_error("✅ Django configurado correctamente")
        
        # Verificar configuración de archivos estáticos
        from django.conf import settings
        
        static_info = {
            'STATIC_URL': getattr(settings, 'STATIC_URL', 'No configurado'),
            'STATIC_ROOT': getattr(settings, 'STATIC_ROOT', 'No configurado'),
            'STATICFILES_DIRS': getattr(settings, 'STATICFILES_DIRS', []),
        }
        
        log_error(f"📊 Configuración de archivos estáticos: {static_info}")
        
        # Verificar si STATIC_ROOT existe
        if static_info['STATIC_ROOT'] != 'No configurado':
            exists = os.path.exists(static_info['STATIC_ROOT'])
            log_error(f"📁 STATIC_ROOT existe: {exists}")
            
            if exists:
                try:
                    files = os.listdir(static_info['STATIC_ROOT'])
                    log_error(f"📄 Archivos en STATIC_ROOT: {files[:10]}...")  # Solo los primeros 10
                except Exception as e:
                    log_error("❌ Error al listar archivos en STATIC_ROOT", e)
        
        return True
        
    except Exception as e:
        log_error("❌ Error al configurar Django", e)
        return False

def main():
    """Función principal"""
    log_error("🚀 Iniciando diagnóstico de Django")
    
    # Verificar Python
    log_error(f"🐍 Versión de Python: {sys.version}")
    log_error(f"📁 Directorio actual: {os.getcwd()}")
    log_error(f"📁 Archivos en el directorio: {os.listdir('.')}")
    
    # Verificar Django
    if check_django_setup():
        log_error("🎉 Diagnóstico completado exitosamente")
    else:
        log_error("💥 Diagnóstico falló")

if __name__ == '__main__':
    main() 