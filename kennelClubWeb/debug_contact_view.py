#!/usr/bin/env python
"""
Script para simular exactamente la vista de contacto y diagnosticar el error 500
"""
import os
import django
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings')
django.setup()

def simulate_contact_view():
    """Simula exactamente lo que hace la vista de contacto"""
    print("🔍 Simulando vista de contacto paso a paso...")
    
    try:
        # Paso 1: Obtener datos del formulario (simulados)
        print("1️⃣ Obteniendo datos del formulario...")
        nombre = "Usuario de Prueba"
        email = "test@example.com"
        asunto = "Prueba de formulario"
        mensaje = "Este es un mensaje de prueba del formulario de contacto."
        
        print(f"   Nombre: {nombre}")
        print(f"   Email: {email}")
        print(f"   Asunto: {asunto}")
        print(f"   Mensaje: {mensaje}")
        
        # Paso 2: Validar campos
        print("\n2️⃣ Validando campos...")
        if not all([nombre, email, asunto, mensaje]):
            print("❌ Error: Campos incompletos")
            return False
        print("✅ Validación de campos exitosa")
        
        # Paso 3: Crear contenido del correo
        print("\n3️⃣ Creando contenido del correo...")
        email_content = f"""
Nuevo mensaje de contacto desde el sitio web Kennel Club de Chile

Nombre: {nombre}
Email: {email}
Asunto: {asunto}

Mensaje:
{mensaje}

---
Este mensaje fue enviado desde el formulario de contacto del sitio web.
        """
        print("✅ Contenido del correo creado")
        
        # Paso 4: Enviar correo
        print("\n4️⃣ Enviando correo...")
        print(f"   From: {settings.EMAIL_HOST_USER}")
        print(f"   To: {settings.EMAIL_HOST_USER}")
        print(f"   Subject: Nuevo mensaje de contacto: {asunto}")
        
        send_mail(
            subject=f'Nuevo mensaje de contacto: {asunto}',
            message=email_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        print("✅ Correo enviado exitosamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error en la simulación: {e}")
        print(f"   Tipo de error: {type(e).__name__}")
        print(f"   Línea donde ocurrió: {e.__traceback__.tb_lineno}")
        return False

def test_imports():
    """Prueba que todos los imports necesarios funcionen"""
    print("🔍 Probando imports necesarios...")
    
    try:
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
        
        from django.core.mail import send_mail
        print("✅ django.core.mail importado")
        
        from django.contrib import messages
        print("✅ django.contrib.messages importado")
        
        from django.conf import settings
        print("✅ django.conf importado")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en imports: {e}")
        return False

def test_settings_access():
    """Prueba acceso a configuraciones"""
    print("\n🔍 Probando acceso a configuraciones...")
    
    try:
        print(f"   EMAIL_HOST: {settings.EMAIL_HOST}")
        print(f"   EMAIL_PORT: {settings.EMAIL_PORT}")
        print(f"   EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
        print(f"   EMAIL_HOST_PASSWORD: {'*' * len(settings.EMAIL_HOST_PASSWORD)}")
        print(f"   DEBUG: {settings.DEBUG}")
        print(f"   SECRET_KEY: {'*' * len(settings.SECRET_KEY)}")
        return True
        
    except Exception as e:
        print(f"❌ Error accediendo a settings: {e}")
        return False

def main():
    print("🚀 Diagnóstico completo de la vista de contacto...")
    print("=" * 60)
    
    # Probar imports
    imports_ok = test_imports()
    
    # Probar acceso a settings
    settings_ok = test_settings_access()
    
    # Simular vista de contacto
    view_ok = simulate_contact_view()
    
    print("\n" + "=" * 60)
    print("📊 RESUMEN DEL DIAGNÓSTICO:")
    print(f"   Imports: {'✅ OK' if imports_ok else '❌ FALLO'}")
    print(f"   Settings: {'✅ OK' if settings_ok else '❌ FALLO'}")
    print(f"   Vista de contacto: {'✅ OK' if view_ok else '❌ FALLO'}")
    
    if not view_ok:
        print("\n💡 POSIBLES CAUSAS DEL ERROR 500:")
        print("   1. Problema con el manejo de mensajes de Django")
        print("   2. Error en el template de contacto")
        print("   3. Problema con CSRF token")
        print("   4. Error en el manejo de la request")
        print("   5. Problema con el redirect después del envío")

if __name__ == "__main__":
    main() 