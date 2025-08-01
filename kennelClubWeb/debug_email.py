#!/usr/bin/env python
"""
Script de debug para probar la configuración de correo y diagnosticar errores
"""
import os
import django
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail
from django.conf import settings

# Configurar Django para DESARROLLO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings')
django.setup()

def test_smtp_connection():
    """Prueba la conexión SMTP directamente"""
    print("🔍 Probando conexión SMTP directa...")
    
    try:
        # Crear contexto SSL
        context = ssl.create_default_context()
        
        # Intentar conexión
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as server:
            print(f"✅ Conexión SSL exitosa a {settings.EMAIL_HOST}:{settings.EMAIL_PORT}")
            
            # Intentar login
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            print("✅ Login exitoso")
            
            return True
            
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Error de autenticación: {e}")
        return False
    except smtplib.SMTPConnectError as e:
        print(f"❌ Error de conexión: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_django_email():
    """Prueba el envío de correo usando Django"""
    print("\n🔍 Probando envío con Django...")
    
    try:
        send_mail(
            subject='Prueba de debug - Django',
            message='Este es un mensaje de prueba para debug.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        print("✅ Correo enviado exitosamente con Django!")
        return True
    except Exception as e:
        print(f"❌ Error al enviar con Django: {e}")
        print(f"   Tipo de error: {type(e).__name__}")
        return False

def show_email_config():
    """Muestra la configuración actual de correo"""
    print("📧 Configuración actual de correo:")
    print(f"   EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    print(f"   EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"   EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"   EMAIL_USE_SSL: {settings.EMAIL_USE_SSL}")
    print(f"   EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    print(f"   EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"   EMAIL_HOST_PASSWORD: {'*' * len(settings.EMAIL_HOST_PASSWORD)}")
    print()

def test_contact_form_simulation():
    """Simula el envío del formulario de contacto"""
    print("\n🔍 Simulando formulario de contacto...")
    
    try:
        # Datos simulados del formulario
        nombre = "Usuario de Prueba"
        email = "test@example.com"
        asunto = "Prueba de formulario"
        mensaje = "Este es un mensaje de prueba del formulario de contacto."
        
        # Crear el contenido del correo (igual que en la vista)
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
        
        # Enviar el correo
        send_mail(
            subject=f'Nuevo mensaje de contacto: {asunto}',
            message=email_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        print("✅ Formulario de contacto simulado exitosamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error en simulación del formulario: {e}")
        print(f"   Tipo de error: {type(e).__name__}")
        return False

def main():
    print("🚀 Iniciando debug de configuración de correo...")
    print("=" * 50)
    
    # Mostrar configuración
    show_email_config()
    
    # Probar conexión SMTP
    smtp_ok = test_smtp_connection()
    
    # Probar Django
    django_ok = test_django_email()
    
    # Probar formulario de contacto
    form_ok = test_contact_form_simulation()
    
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"   Conexión SMTP: {'✅ OK' if smtp_ok else '❌ FALLO'}")
    print(f"   Django Email: {'✅ OK' if django_ok else '❌ FALLO'}")
    print(f"   Formulario Contacto: {'✅ OK' if form_ok else '❌ FALLO'}")
    
    if not any([smtp_ok, django_ok, form_ok]):
        print("\n💡 SUGERENCIAS:")
        print("   1. Verifica que las credenciales sean correctas")
        print("   2. Confirma que el servidor SMTP esté disponible")
        print("   3. Revisa si necesitas habilitar 'Acceso de aplicaciones menos seguras'")
        print("   4. Verifica que el puerto 465 esté abierto")

if __name__ == "__main__":
    main() 