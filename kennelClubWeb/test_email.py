#!/usr/bin/env python
"""
Script de prueba para verificar la configuración de correo
"""
import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kennelClubWeb.settings')
django.setup()

def test_email():
    try:
        send_mail(
            subject='Prueba de correo desde Django',
            message='Este es un mensaje de prueba para verificar la configuración SMTP.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        print("✅ Correo enviado exitosamente!")
        return True
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
        return False

if __name__ == "__main__":
    print("Probando configuración de correo...")
    test_email() 