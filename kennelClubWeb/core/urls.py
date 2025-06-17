from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<int:noticia_id>/', views.detalle_noticia, name="detalle_noticia"),
    path('crianza/', views.crianza, name="crianza"),
]