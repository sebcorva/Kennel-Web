#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar y corregir permisos de archivos en cPanel
"""
import os
import stat
import sys

def check_and_fix_permissions():
    """Verifica y corrige permisos de archivos"""
    print("🔧 Verificando y corrigiendo permisos de archivos...")
    
    # Directorios que necesitan permisos específicos
    directories = [
        'staticfiles',
        'staticfiles/admin',
        'staticfiles/css',
        'staticfiles/img',
        'staticfiles/js',
        'media',
        'static',
        'static/css',
        'static/img',
    ]
    
    # Archivos que necesitan permisos específicos
    file_patterns = [
        '*.css',
        '*.js',
        '*.png',
        '*.jpg',
        '*.jpeg',
        '*.gif',
        '*.ico',
        '*.svg',
    ]
    
    print("\n📁 Verificando directorios...")
    for directory in directories:
        if os.path.exists(directory):
            current_perms = oct(os.stat(directory).st_mode)[-3:]
            print(f"  {directory}: {current_perms}")
            
            # Corregir permisos de directorios (755)
            try:
                os.chmod(directory, 0o755)
                new_perms = oct(os.stat(directory).st_mode)[-3:]
                print(f"    ✅ Corregido: {new_perms}")
            except Exception as e:
                print(f"    ❌ Error: {e}")
        else:
            print(f"  {directory}: ❌ No existe")
    
    print("\n📄 Verificando archivos estáticos...")
    static_files = []
    
    # Buscar archivos estáticos
    for root, dirs, files in os.walk('staticfiles'):
        for file in files:
            if any(file.endswith(ext) for ext in ['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg']):
                file_path = os.path.join(root, file)
                static_files.append(file_path)
    
    print(f"  Encontrados {len(static_files)} archivos estáticos")
    
    # Corregir permisos de archivos (644)
    for file_path in static_files[:10]:  # Solo los primeros 10 para no saturar
        try:
            current_perms = oct(os.stat(file_path).st_mode)[-3:]
            os.chmod(file_path, 0o644)
            new_perms = oct(os.stat(file_path).st_mode)[-3:]
            print(f"    {file_path}: {current_perms} → {new_perms}")
        except Exception as e:
            print(f"    ❌ Error en {file_path}: {e}")
    
    if len(static_files) > 10:
        print(f"    ... y {len(static_files) - 10} archivos más")
    
    print("\n✅ Verificación de permisos completada")

def check_file_accessibility():
    """Verifica si los archivos son accesibles"""
    print("\n🔍 Verificando accesibilidad de archivos...")
    
    test_files = [
        'staticfiles/admin/css/base.css',
        'staticfiles/css/style.css',
        'staticfiles/img/kennel-club-chile.png',
    ]
    
    for file_path in test_files:
        if os.path.exists(file_path):
            try:
                # Verificar si se puede leer
                with open(file_path, 'rb') as f:
                    f.read(1)
                print(f"  ✅ {file_path}: Accesible")
            except Exception as e:
                print(f"  ❌ {file_path}: Error de acceso - {e}")
        else:
            print(f"  ❌ {file_path}: No existe")

def main():
    """Función principal"""
    print("🚀 Verificador de permisos para Kennel Club Chile")
    print("=" * 50)
    
    # Verificar permisos
    check_and_fix_permissions()
    
    # Verificar accesibilidad
    check_file_accessibility()
    
    print("\n📋 Instrucciones:")
    print("1. Si los permisos se corrigieron, prueba acceder a los archivos")
    print("2. Si hay errores, contacta al soporte de tu hosting")
    print("3. Verifica que el directorio 'staticfiles' esté en la raíz del sitio")

if __name__ == '__main__':
    main() 