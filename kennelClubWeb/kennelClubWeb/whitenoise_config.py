"""
Configuración personalizada para WhiteNoise para servir archivos media
"""
import os
from whitenoise import WhiteNoise
from django.conf import settings

class MediaWhiteNoise(WhiteNoise):
    """
    Extensión de WhiteNoise para servir archivos media
    """
    def __init__(self, application, media_root=None, **kwargs):
        super().__init__(application, **kwargs)
        self.media_root = media_root or settings.MEDIA_ROOT
        self.add_files(self.media_root, prefix=settings.MEDIA_URL.strip('/'))

def get_media_whitenoise(application):
    """
    Función para crear una instancia de WhiteNoise configurada para media
    """
    return MediaWhiteNoise(
        application,
        media_root=settings.MEDIA_ROOT,
        autorefresh=True,
        max_age=31536000,  # 1 año
        add_headers_function=lambda headers, path, url: headers
    ) 