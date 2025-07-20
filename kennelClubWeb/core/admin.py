from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import CategoriaNoticias, Noticias, Raza, Especialidad, TipoJuez, Licencia, Juez, Evento, Ranking, Reglamentos, Crianza, HistoriaRazas, FotoHistoriaRaza, Club, Tramites, ArchivoTramite, PreguntasFrecuentes

class CategoriaNoticiasForm(forms.ModelForm):
    COLOR_CHOICES = [
        ('', 'Sin color'),
        ('#3b82f6', 'Azul'),
        ('#10b981', 'Verde'),
        ('#ef4444', 'Rojo'),
        ('#8b5cf6', 'Morado'),
        ('#eab308', 'Amarillo'),
        ('#6366f1', 'Índigo'),
        ('#ec4899', 'Rosa'),
        ('#14b8a6', 'Verde Azulado'),
        ('#f97316', 'Naranja'),
        ('#6b7280', 'Gris'),
    ]
    
    color_selector = forms.ChoiceField(
        choices=COLOR_CHOICES,
        label='Seleccionar Color',
        required=False,
        widget=forms.Select(attrs={
            'class': 'color-selector',
            'style': 'width: 200px; padding: 8px; border-radius: 4px; border: 1px solid #ddd;'
        })
    )
    
    class Meta:
        model = CategoriaNoticias
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.color:
            # Si es una edición y tiene color, seleccionar el color actual
            self.fields['color_selector'].initial = self.instance.color
    
    def clean(self):
        cleaned_data = super().clean()
        color_selector = cleaned_data.get('color_selector')
        
        if color_selector:
            cleaned_data['color'] = color_selector
        
        return cleaned_data

@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'categorias_display')
    list_filter = ('categorias', 'fecha')
    search_fields = ('titulo', 'texto')
    date_hierarchy = 'fecha'
    filter_horizontal = ('categorias',)
    formfield_overrides = {
        'texto': {'widget': CKEditor5Widget(config_name='extends')}
    }
    
    def categorias_display(self, obj):
        return ", ".join([cat.nombre for cat in obj.categorias.all()])
    categorias_display.short_description = 'Categorías'

@admin.register(CategoriaNoticias)
class CategoriaNoticiasAdmin(admin.ModelAdmin):
    form = CategoriaNoticiasForm
    list_display = ('nombre', 'codigo_categoria', 'color', 'color_preview')
    search_fields = ('nombre', 'codigo_categoria')
    ordering = ('nombre',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'codigo_categoria')
        }),
        ('Color de la Categoría', {
            'fields': ('color_selector', 'color'),
            'description': 'Selecciona un color de la lista desplegable. El color se aplicará automáticamente al campo "Color".'
        }),
    )
    
    def color_preview(self, obj):
        if obj.color:
            # Mapeo de nombres de colores para la vista previa
            color_names = {
                '#3b82f6': 'Azul',
                '#10b981': 'Verde',
                '#ef4444': 'Rojo',
                '#8b5cf6': 'Morado',
                '#eab308': 'Amarillo',
                '#6366f1': 'Índigo',
                '#ec4899': 'Rosa',
                '#14b8a6': 'Verde Azulado',
                '#f97316': 'Naranja',
                '#6b7280': 'Gris',
            }
            
            color_name = color_names.get(obj.color, 'Personalizado')
            
            return format_html(
                '<span style="background-color: {}; padding: 4px 8px; border-radius: 4px; color: #1f2937; font-size: 12px; font-weight: 500; border: 1px solid #d1d5db;">{}</span>',
                obj.color,
                color_name
            )
        return "Sin color"
    color_preview.short_description = 'Vista previa'
    
    class Media:
        css = {
            'all': ('admin/css/categoria_color.css',)
        }

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


class RankingAdminForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = '__all__'
        widgets = {
            'fecha': forms.TextInput(
                attrs={
                    'placeholder': 'YYYY-MM (ej: 2024-01)',
                    'class': 'vTextField',
                }
            ),
        }

@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    form = RankingAdminForm
    list_display = ('titulo', 'fecha_mes_anio', 'archivo', 'categoria')
    list_filter = ('fecha', 'categoria')
    search_fields = ('titulo', 'categoria')
    fieldsets = (
        ('Información del Ranking', {
            'fields': ('titulo', 'fecha', 'archivo', 'categoria')
        }),
    )
    ordering = ('-fecha',)
    
    def fecha_mes_anio(self, obj):
        return obj.fecha_mes_anio()
    fecha_mes_anio.short_description = 'Mes/Año'


@admin.register(Reglamentos)
class ReglamentosAdmin(admin.ModelAdmin):
    list_display = ('nombreReglamento', 'archivo', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('nombreReglamento',)
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Información del Reglamento', {
            'fields': ('nombreReglamento', 'archivo')
        }),
        ('Información del Sistema', {
            'fields': ('fecha_creacion',)
        }),
    )
    ordering = ('-fecha_creacion',)


@admin.register(Crianza)
class CrianzaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo', 'contenido')
    formfield_overrides = {
        'contenido': {'widget': CKEditor5Widget(config_name='extends')}
    }
    fieldsets = (
        ('Información de Crianza', {
            'fields': ('titulo', 'contenido')
        }),
    )
    ordering = ('titulo',)


class FotoHistoriaRazaInline(admin.TabularInline):
    model = FotoHistoriaRaza
    extra = 1
    fields = ('imagen', 'orden')


@admin.register(HistoriaRazas)
class HistoriaRazasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen_preview', 'fecha_creacion')
    list_filter = ('fecha_creacion', 'clubes')
    search_fields = ('titulo',)
    readonly_fields = ('fecha_creacion', 'imagen_preview')
    inlines = [FotoHistoriaRazaInline]
    filter_horizontal = ('clubes',)
    fieldsets = (
        ('Información de la Historia', {
            'fields': ('titulo', 'imagenPrincipal')
        }),
        ('Clubes Relacionados', {
            'fields': ('clubes',)
        }),
        ('Información del Sistema', {
            'fields': ('fecha_creacion', 'imagen_preview')
        }),
    )
    ordering = ('-fecha_creacion',)
    
    def imagen_preview(self, obj):
        if obj.imagenPrincipal:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.imagenPrincipal.url)
        return "Sin imagen principal"
    imagen_preview.short_description = 'Imagen Principal'


@admin.register(FotoHistoriaRaza)
class FotoHistoriaRazaAdmin(admin.ModelAdmin):
    list_display = ('historia_raza', 'orden', 'imagen_preview')
    list_filter = ('historia_raza', 'orden')
    search_fields = ('historia_raza__titulo',)
    list_editable = ('orden',)
    fieldsets = (
        ('Información de la Foto', {
            'fields': ('historia_raza', 'imagen', 'orden')
        }),
    )
    ordering = ('historia_raza', 'orden', 'id')
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.imagen.url)
        return "Sin imagen"
    imagen_preview.short_description = 'Vista previa'


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'logo_preview', 'link')
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('logo_preview',)
    formfield_overrides = {
        'descripcion': {'widget': CKEditor5Widget(config_name='extends')}
    }
    fieldsets = (
        ('Información del Club', {
            'fields': ('titulo', 'descripcion', 'logo', 'link')
        }),
    )
    ordering = ('titulo',)
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.logo.url)
        return "Sin logo"
    logo_preview.short_description = 'Logo'


class ArchivoTramiteInline(admin.TabularInline):
    model = ArchivoTramite
    extra = 1
    fields = ('archivo', 'nombre_archivo')


@admin.register(Tramites)
class TramitesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen_preview')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('imagen_preview',)
    inlines = [ArchivoTramiteInline]
    fieldsets = (
        ('Información del Trámite', {
            'fields': ('nombre', 'descripcion', 'imagen')
        }),
    )
    ordering = ('nombre',)
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.imagen.url)
        return "Sin imagen"
    imagen_preview.short_description = 'Imagen'


@admin.register(ArchivoTramite)
class ArchivoTramiteAdmin(admin.ModelAdmin):
    list_display = ('tramite', 'nombre_archivo', 'archivo_preview', 'fecha_subida')
    list_filter = ('tramite', 'fecha_subida')
    search_fields = ('tramite__nombre', 'nombre_archivo')
    readonly_fields = ('fecha_subida', 'archivo_preview')
    fieldsets = (
        ('Información del Archivo', {
            'fields': ('tramite', 'archivo', 'nombre_archivo')
        }),
        ('Información del Sistema', {
            'fields': ('fecha_subida', 'archivo_preview')
        }),
    )
    ordering = ('-fecha_subida',)
    
    def archivo_preview(self, obj):
        if obj.archivo:
            return format_html('<a href="{}" target="_blank">Ver archivo</a>', obj.archivo.url)
        return "Sin archivo"
    archivo_preview.short_description = 'Archivo'


@admin.register(PreguntasFrecuentes)
class PreguntasFrecuentesAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'categoria', 'orden')
    list_filter = ('categoria',)
    search_fields = ('pregunta', 'respuesta')
    list_editable = ('orden',)
    fieldsets = (
        ('Información de la Pregunta', {
            'fields': ('pregunta', 'respuesta', 'categoria')
        }),
        ('Configuración', {
            'fields': ('orden',)
        }),
    )
    ordering = ('categoria', 'orden')
