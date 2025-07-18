from django.db import models
from django.core.validators import RegexValidator
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class CategoriaNoticias(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo_categoria = models.CharField(max_length=50, unique=True, help_text="Código único para identificar la categoría")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría de Noticias'
        verbose_name_plural = 'Categorías de Noticias'
        ordering = ['nombre']


class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    texto = CKEditor5Field(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    categorias = models.ManyToManyField(CategoriaNoticias, related_name='noticias', blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'


class Raza(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'


class TipoJuez(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Tipo de Juez'
        verbose_name_plural = 'Tipos de Juez'


class Licencia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Licencia'
        verbose_name_plural = 'Licencias'


class Juez(models.Model):
    nombres = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True, null=True, blank=True)
    fotografia = models.ImageField(upload_to='jueces/', null=True, blank=True)
    email = models.EmailField()
    celular1 = models.CharField(max_length=20)
    celular2 = models.CharField(max_length=20, blank=True, null=True)
    afijo = models.CharField(max_length=100, blank=True, null=True)
    razas = models.ManyToManyField(Raza, related_name='jueces')
    especialidades = models.ManyToManyField(Especialidad, related_name='jueces')
    curriculum = models.FileField(upload_to='curriculums/', blank=True, null=True)
    tipo_juez = models.ForeignKey(TipoJuez, on_delete=models.CASCADE)
    licencias = models.ManyToManyField(Licencia, related_name='jueces', blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
    
    def nombre_completo(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
    
    class Meta:
        verbose_name = 'Juez'
        verbose_name_plural = 'Jueces'
        ordering = ['apellido_paterno', 'apellido_materno', 'nombres']


class Evento(models.Model):
    tipo_evento = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    lugar = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    invitados = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tipo_evento} - {self.lugar}"
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-fecha_inicio']


class Ranking(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex=r'^\d{4}-\d{2}$',
                message='Ingresa la fecha en formato YYYY-MM (ej: 2024-01)'
            )
        ],
        help_text="Formato: YYYY-MM (ej: 2024-01 para Enero 2024)"
    )
    archivo = models.FileField(upload_to='rankings/', blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    def fecha_mes_anio(self):
        """Retorna la fecha en formato mes/año en español"""
        try:
            from datetime import datetime
            fecha_obj = datetime.strptime(self.fecha, '%Y-%m')
            
            # Diccionario para convertir meses a español
            meses_es = {
                1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
                7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
            }
            
            mes_es = meses_es[fecha_obj.month]
            año = fecha_obj.year
            
            return f"{mes_es} {año}"
        except:
            return self.fecha
    
    class Meta:
        verbose_name = 'Ranking'
        verbose_name_plural = 'Rankings'
        ordering = ['-fecha']


class Reglamentos(models.Model):
    nombreReglamento = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='reglamentos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombreReglamento
    
    class Meta:
        verbose_name = 'Reglamento'
        verbose_name_plural = 'Reglamentos'
        ordering = ['-fecha_creacion']


class Crianza(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = CKEditor5Field(blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Crianza'
        verbose_name_plural = 'Crianza'


class Club(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = CKEditor5Field(blank=True, null=True)
    logo = models.ImageField(upload_to='clubes/', null=True, blank=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubes'
        ordering = ['titulo']


class HistoriaRazas(models.Model):
    titulo = models.CharField(max_length=200)
    imagenPrincipal = models.ImageField(upload_to='historia_razas/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    clubes = models.ManyToManyField(Club, related_name='historias_razas', blank=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Historia de Raza'
        verbose_name_plural = 'Historias de Razas'
        ordering = ['-fecha_creacion']


class FotoHistoriaRaza(models.Model):
    historia_raza = models.ForeignKey(HistoriaRazas, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='historia_razas/')
    orden = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Foto de {self.historia_raza.titulo} - Orden {self.orden}"
    
    class Meta:
        verbose_name = 'Foto de Historia de Raza'
        verbose_name_plural = 'Fotos de Historias de Razas'
        ordering = ['orden', 'id']


class Tramites(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='tramites/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Trámite'
        verbose_name_plural = 'Trámites'
        ordering = ['nombre']


class ArchivoTramite(models.Model):
    tramite = models.ForeignKey(Tramites, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to='tramites/')
    nombre_archivo = models.CharField(max_length=200, blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Archivo de {self.tramite.nombre}"
    
    def save(self, *args, **kwargs):
        if not self.nombre_archivo:
            self.nombre_archivo = self.archivo.name.split('/')[-1]
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Archivo de Trámite'
        verbose_name_plural = 'Archivos de Trámites'
        ordering = ['fecha_subida']


class PreguntasFrecuentes(models.Model):
    CATEGORIA_CHOICES = [
        ('tramites', 'Trámites y Documentación'),
        ('cruza', 'Cruza y Camadas'),
        ('exposiciones', 'Exposiciones y Campeonatos'),
        ('contacto', 'Contacto y Horarios'),
    ]
    
    pregunta = models.CharField(max_length=500)
    respuesta = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    orden = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.pregunta
    
    class Meta:
        verbose_name = 'Pregunta Frecuente'
        verbose_name_plural = 'Preguntas Frecuentes'
        ordering = ['categoria', 'orden']

