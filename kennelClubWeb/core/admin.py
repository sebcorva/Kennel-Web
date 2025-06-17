from django.contrib import admin
from .models import Noticias

@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'categoria')
    list_filter = ('categoria', 'fecha')
    search_fields = ('titulo', 'texto')
    date_hierarchy = 'fecha'
