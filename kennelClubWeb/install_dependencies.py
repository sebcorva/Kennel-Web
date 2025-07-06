#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para instalar dependencias de Django en cPanel
"""
import os
import sys
import subprocess

def install_requirements():
    print("🚀 Instalando dependencias de Django...")
    
    # Ruta al archivo requirements.txt
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    
    if not os.path.exists(requirements_file):
        print(f"❌ ERROR: No se encontró el archivo requirements.txt en {requirements_file}")
        return False
    
    try:
        # Instalar dependencias usando pip
        print("📦 Instalando paquetes desde requirements.txt...")
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', requirements_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencias instaladas correctamente")
            print("📋 Salida del comando:")
            print(result.stdout)
            return True
        else:
            print("❌ ERROR al instalar dependencias:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def check_django():
    print("\n🔍 Verificando instalación de Django...")
    
    try:
        import django
        print(f"✅ Django instalado correctamente - Versión: {django.get_version()}")
        return True
    except ImportError:
        print("❌ Django no está instalado")
        return False

def main():
    print("🔧 Instalador de dependencias para Kennel Club Chile")
    print("=" * 50)
    
    # Instalar dependencias
    if install_requirements():
        # Verificar Django
        if check_django():
            print("\n🎉 ¡Todas las dependencias instaladas correctamente!")
            print("📋 Ahora puedes reiniciar tu aplicación en cPanel")
        else:
            print("\n⚠️ Las dependencias se instalaron pero Django no se puede importar")
            print("📋 Verifica la configuración de Python en cPanel")
    else:
        print("\n💥 Error al instalar dependencias")
        print("📋 Verifica los logs de error arriba")

if __name__ == '__main__':
    main() 