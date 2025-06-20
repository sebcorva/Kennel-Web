from django.db import models
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    texto = RichTextUploadingField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)
    categoria = models.CharField(max_length=100)

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
        """Retorna la fecha en formato mes/año"""
        try:
            from datetime import datetime
            fecha_obj = datetime.strptime(self.fecha, '%Y-%m')
            return fecha_obj.strftime('%B %Y')
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
    contenido = RichTextUploadingField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Crianza'
        verbose_name_plural = 'Crianza'

