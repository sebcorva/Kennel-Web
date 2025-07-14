from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sitemap.xml', views.sitemap_xml, name="sitemap_xml"),
    path('robots.txt', views.robots_txt, name="robots_txt"),
    path('login/', views.login, name="login"),
    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<int:noticia_id>/', views.detalle_noticia, name="detalle_noticia"),
    path('crianza/', views.crianza, name="crianza"),
    path('jueces-nacionales/', views.jueces_nacionales, name="jueces_nacionales"),
    path('eventos/', views.eventos, name="eventos"),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('razas/', views.razas, name='razas'),
    path('historia-razas/', views.historia_razas, name='historia_razas'),
    path('historia-razas/<int:historia_id>/', views.detalle_historia_raza, name='detalle_historia_raza'),
    path('rankings/', views.rankings, name='rankings'),
    path('reglamentos/', views.reglamentos, name='reglamentos'),
    path('tramites/', views.tramites, name='tramites'),
    path('preguntas-frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('preguntas-frecuentes/<str:categoria>/', views.detalle_preguntas_frecuentes, name='detalle_preguntas_frecuentes'),
    path('contacto/', views.contacto, name='contacto'),
]