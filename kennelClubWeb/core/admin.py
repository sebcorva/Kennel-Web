from django.contrib import admin
from .models import Noticias, Raza, Especialidad, TipoJuez, Licencia, Juez, Evento

@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'categoria')
    list_filter = ('categoria', 'fecha')
    search_fields = ('titulo', 'texto')
    date_hierarchy = 'fecha'


@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


@admin.register(TipoJuez)
class TipoJuezAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


@admin.register(Licencia)
class LicenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


@admin.register(Juez)
class JuezAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido_paterno', 'apellido_materno', 'rut', 'tipo_juez', 'activo')
    list_filter = ('tipo_juez', 'activo', 'razas', 'especialidades', 'licencias')
    search_fields = ('nombres', 'apellido_paterno', 'apellido_materno', 'rut', 'email', 'afijo')
    filter_horizontal = ('razas', 'especialidades', 'licencias')
    readonly_fields = ('fecha_registro',)
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombres', 'apellido_paterno', 'apellido_materno', 'rut', 'fotografia')
        }),
        ('Contacto', {
            'fields': ('email', 'celular1', 'celular2')
        }),
        ('Información Profesional', {
            'fields': ('afijo', 'tipo_juez', 'razas', 'especialidades', 'licencias')
        }),
        ('Documentos', {
            'fields': ('curriculum',)
        }),
        ('Estado', {
            'fields': ('activo', 'fecha_registro')
        }),
    )
    ordering = ('apellido_paterno', 'apellido_materno', 'nombres')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('tipo_evento', 'fecha_inicio', 'fecha_termino', 'lugar')
    list_filter = ('tipo_evento', 'fecha_inicio', 'fecha_termino')
    search_fields = ('tipo_evento', 'lugar', 'descripcion', 'invitados')
    readonly_fields = ('fecha_creacion',)
    date_hierarchy = 'fecha_inicio'
    fieldsets = (
        ('Información del Evento', {
            'fields': ('tipo_evento', 'descripcion')
        }),
        ('Fechas y Lugar', {
            'fields': ('fecha_inicio', 'fecha_termino', 'lugar')
        }),
        ('Invitados', {
            'fields': ('invitados',)
        }),
        ('Información del Sistema', {
            'fields': ('fecha_creacion',)
        }),
    )
    ordering = ('-fecha_inicio',)
