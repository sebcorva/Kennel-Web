#!/usr/bin/env python
"""
Script para probar que todos los imports funcionan correctamente
"""
import os
import sys

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings')
import django
django.setup()

def test_imports():
    """Prueba todos los imports necesarios"""
    print("🔍 Probando imports necesarios...")
    
    try:
        # Imports básicos de Django
        from django.contrib.auth import authenticate, login
        print("✅ django.contrib.auth importado")
        
        from django.shortcuts import render, redirect, get_object_or_404
        print("✅ django.shortcuts importado")
        
        from django.http import HttpResponse
        print("✅ django.http importado")
        
        from django.template.loader import render_to_string
        print("✅ django.template.loader importado")
        
        from django.utils import timezone
        print("✅ django.utils importado")
        
        from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
        print("✅ django.core.paginator importado")
        
        # Import crítico para el correo
        from django.core.mail import send_mail
        print("✅ django.core.mail importado")
        
        from django.contrib import messages
        print("✅ django.contrib.messages importado")
        
        from django.conf import settings
        print("✅ django.conf importado")
        
        # Imports de modelos
        from core.models import Noticias, Juez, TipoJuez, Evento, Ranking, Reglamentos, Crianza, HistoriaRazas, FotoHistoriaRaza, Tramites, PreguntasFrecuentes
        print("✅ Modelos importados")
        
        # Imports de datetime
        from datetime import datetime, timedelta
        print("✅ datetime importado")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en imports: {e}")
        print(f"   Tipo de error: {type(e).__name__}")
        return False

def test_send_mail_function():
    """Prueba específicamente la función send_mail"""
    print("\n🔍 Probando función send_mail...")
    
    try:
        from django.core.mail import send_mail
        from django.conf import settings
        
        print(f"   send_mail está disponible: {send_mail is not None}")
        print(f"   EMAIL_HOST: {settings.EMAIL_HOST}")
        print(f"   EMAIL_PORT: {settings.EMAIL_PORT}")
        print(f"   EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error con send_mail: {e}")
        return False

def test_contact_view_imports():
    """Prueba los imports específicos de la vista de contacto"""
    print("\n🔍 Probando imports de la vista de contacto...")
    
    try:
        # Simular los imports que hace la vista de contacto
        from django.core.mail import send_mail
        from django.conf import settings
        from django.http import HttpResponse
        
        # Probar que send_mail es callable
        if callable(send_mail):
            print("✅ send_mail es una función válida")
        else:
            print("❌ send_mail no es una función válida")
            
        return True
        
    except Exception as e:
        print(f"❌ Error en imports de vista de contacto: {e}")
        return False

def main():
    print("🚀 Probando imports del proyecto...")
    print("=" * 50)
    
    # Probar imports generales
    imports_ok = test_imports()
    
    # Probar función send_mail específicamente
    send_mail_ok = test_send_mail_function()
    
    # Probar imports de la vista de contacto
    contact_imports_ok = test_contact_view_imports()
    
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"   Imports generales: {'✅ OK' if imports_ok else '❌ FALLO'}")
    print(f"   Función send_mail: {'✅ OK' if send_mail_ok else '❌ FALLO'}")
    print(f"   Imports vista contacto: {'✅ OK' if contact_imports_ok else '❌ FALLO'}")
    
    if not all([imports_ok, send_mail_ok, contact_imports_ok]):
        print("\n💡 POSIBLES SOLUCIONES:")
        print("   1. Verificar que Django esté instalado correctamente")
        print("   2. Revisar la configuración de settings")
        print("   3. Verificar que no haya conflictos de nombres")
        print("   4. Reiniciar el servidor web")

if __name__ == "__main__":
    main() 