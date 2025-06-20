from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<int:noticia_id>/', views.detalle_noticia, name="detalle_noticia"),
    path('crianza/', views.crianza, name="crianza"),
    path('jueces-nacionales/', views.jueces_nacionales, name="jueces_nacionales"),
    path('eventos/', views.eventos, name="eventos"),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('razas/', views.razas, name='razas'),
    path('historia-razas/', views.historia_razas, name='historia_razas'),
    path('rankings/', views.rankings, name='rankings'),
    path('reglamentos/', views.reglamentos, name='reglamentos'),
]