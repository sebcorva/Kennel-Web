#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar la estructura de directorios y archivos
"""
import os

def check_directory_structure():
    """Verifica la estructura de directorios"""
    print("📁 Verificando estructura de directorios...")
    
    # Estructura esperada
    expected_structure = {
        'staticfiles': {
            'admin': ['css', 'js', 'img'],
            'css': ['style.css', 'output.css'],
            'img': ['kennel-club-chile.png', 'home-dog.jpg'],
            'js': []
        },
        'static': {
            'css': ['style.css'],
            'img': ['kennel-club-chile.png']
        },
        'media': [],
        'templates': ['test.html', 'base.html'],
        'core': ['views.py', 'urls.py'],
        'kennelClubWeb': ['settings.py', 'settings_production.py', 'urls.py']
    }
    
    for directory, expected_contents in expected_structure.items():
        print(f"\n📂 {directory}/")
        if os.path.exists(directory):
            print(f"  ✅ Existe")
            
            if isinstance(expected_contents, list):
                # Es un directorio con archivos esperados
                for file in expected_contents:
                    file_path = os.path.join(directory, file)
                    if os.path.exists(file_path):
                        print(f"    ✅ {file}")
                    else:
                        print(f"    ❌ {file} - No existe")
            else:
                # Es un directorio con subdirectorios
                for subdir, files in expected_contents.items():
                    subdir_path = os.path.join(directory, subdir)
                    if os.path.exists(subdir_path):
                        print(f"    ✅ {subdir}/")
                        for file in files:
                            file_path = os.path.join(subdir_path, file)
                            if os.path.exists(file_path):
                                print(f"      ✅ {file}")
                            else:
                                print(f"      ❌ {file} - No existe")
                    else:
                        print(f"    ❌ {subdir}/ - No existe")
        else:
            print(f"  ❌ No existe")

def check_static_files():
    """Verifica archivos estáticos específicos"""
    print("\n🔍 Verificando archivos estáticos específicos...")
    
    critical_files = [
        'staticfiles/admin/css/base.css',
        'staticfiles/css/style.css',
        'staticfiles/img/kennel-club-chile.png',
        'staticfiles/img/home-dog.jpg',
        'static/css/style.css',
        'static/img/kennel-club-chile.png'
    ]
    
    for file_path in critical_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"  ✅ {file_path} ({size} bytes)")
        else:
            print(f"  ❌ {file_path} - No existe")

def check_web_access():
    """Verifica si los archivos son accesibles desde la web"""
    print("\n🌐 Verificando acceso web...")
    
    web_paths = [
        '/staticfiles/admin/css/base.css',
        '/staticfiles/css/style.css',
        '/staticfiles/img/kennel-club-chile.png',
        '/static/css/style.css',
        '/static/img/kennel-club-chile.png'
    ]
    
    print("  Prueba estos enlaces en tu navegador:")
    for path in web_paths:
        print(f"    https://kennelclubdechile.cl{path}")

def main():
    """Función principal"""
    print("🚀 Verificador de estructura para Kennel Club Chile")
    print("=" * 50)
    
    # Verificar estructura
    check_directory_structure()
    
    # Verificar archivos estáticos
    check_static_files()
    
    # Verificar acceso web
    check_web_access()
    
    print("\n📋 Recomendaciones:")
    print("1. Si faltan archivos, ejecuta: python manage.py collectstatic")
    print("2. Si los archivos existen pero no se acceden, verifica permisos")
    print("3. Si nada funciona, contacta al soporte de tu hosting")

if __name__ == '__main__':
    main() 