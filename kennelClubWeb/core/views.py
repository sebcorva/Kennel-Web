from django.shortcuts import render, get_object_or_404
from .models import Noticias, Juez, TipoJuez, Evento, Ranking, Reglamentos, Crianza, HistoriaRazas, FotoHistoriaRaza, Tramites, PreguntasFrecuentes
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    return render(request, 'home.html')

def noticias(request):
    noticias = Noticias.objects.all().order_by('-fecha')
    return render(request, 'noticias.html', {'noticias': noticias})

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticias, id=noticia_id)
    return render(request, 'detalle_noticia.html', {'noticia': noticia})

def crianza(request):
    crianzas = Crianza.objects.all().order_by('titulo')
    return render(request, 'crianza.html', {'crianzas': crianzas})

def jueces_nacionales(request):
    # Obtener todos los tipos de juez
    tipos_juez = TipoJuez.objects.all()
    
    # Crear un diccionario con los jueces agrupados por tipo
    jueces_por_tipo = {}
    for tipo in tipos_juez:
        jueces = Juez.objects.filter(tipo_juez=tipo, activo=True).order_by('apellido_paterno', 'apellido_materno', 'nombres')
        if jueces.exists():  # Solo incluir tipos que tengan jueces
            jueces_por_tipo[tipo] = jueces
    
    return render(request, 'jueces_nacionales.html', {
        'jueces_por_tipo': jueces_por_tipo,
        'tipos_juez': tipos_juez
    })

def eventos(request):
    # Obtener parámetros de filtro
    año_filtro = request.GET.get('año')
    mes_filtro = request.GET.get('mes')
    
    # Obtener todos los eventos
    eventos = Evento.objects.all().order_by('-fecha_inicio')
    
    # Aplicar filtros
    if año_filtro:
        eventos = eventos.filter(fecha_inicio__year=año_filtro)
    
    if mes_filtro:
        eventos = eventos.filter(fecha_inicio__month=mes_filtro)
    
    # Diccionario para convertir meses a español
    meses_es = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
        7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    
    # Obtener años únicos de los eventos para el filtro
    años_disponibles = Evento.objects.values_list('fecha_inicio__year', flat=True).distinct().order_by('-fecha_inicio__year')
    
    # Procesar los días de cada evento
    for evento in eventos:
        evento.dias_lista = []
        # Convertir DateField a datetime.date para operaciones
        fecha_actual = evento.fecha_inicio
        fecha_fin = evento.fecha_termino
        
        # Verificar que las fechas sean válidas
        if fecha_actual and fecha_fin and fecha_actual <= fecha_fin:
            while fecha_actual <= fecha_fin:
                evento.dias_lista.append(fecha_actual)
                fecha_actual += timedelta(days=1)
        
        # Formatear los días para mostrar
        evento.dias_formateados = []
        for fecha in evento.dias_lista:
            dia_num = fecha.day
            mes_nombre = meses_es[fecha.month]
            evento.dias_formateados.append(f"{dia_num} {mes_nombre}")
    
    return render(request, 'eventos.html', {
        'eventos': eventos,
        'años_disponibles': años_disponibles,
        'meses_es': meses_es,
        'año_actual': año_filtro,
        'mes_actual': mes_filtro
    })

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def razas(request):
    return render(request, 'razas.html')

def historia_razas(request):
    historias_razas = HistoriaRazas.objects.all().order_by('titulo')
    return render(request, 'historia_razas.html', {'historias_razas': historias_razas})

def rankings(request):
    # Obtener todos los rankings ordenados por fecha (más reciente primero)
    rankings = Ranking.objects.all().order_by('-fecha')
    
    # Agrupar rankings por año
    rankings_por_año = {}
    años_disponibles = []
    
    for ranking in rankings:
        # Extraer el año del campo fecha (formato YYYY-MM)
        año = ranking.fecha.split('-')[0]
        
        if año not in rankings_por_año:
            rankings_por_año[año] = []
            años_disponibles.append(año)
        
        rankings_por_año[año].append(ranking)
    
    # Ordenar años de más reciente a más antiguo
    años_disponibles.sort(reverse=True)
    
    return render(request, 'rankings.html', {
        'rankings_por_año': rankings_por_año,
        'años_disponibles': años_disponibles,
        'rankings': rankings  # Mantener para compatibilidad
    })

def reglamentos(request):
    # Obtener todos los reglamentos ordenados por fecha de creación (más reciente primero)
    reglamentos = Reglamentos.objects.all().order_by('-fecha_creacion')
    
    return render(request, 'reglamentos.html', {
        'reglamentos': reglamentos
    })

def detalle_historia_raza(request, historia_id):
    historia = get_object_or_404(HistoriaRazas, id=historia_id)
    fotos = historia.fotos.all().order_by('orden')
    clubes = historia.clubes.all().order_by('titulo')
    
    return render(request, 'detalle_historia_razas.html', {
        'historia': historia,
        'fotos': fotos,
        'clubes': clubes
    })

def tramites(request):
    # Orden específico solicitado
    orden_especifico = [
        'Trámites a distancia',
        'Obtención de Kennel Name, afijo o nombre de criadero, Declaración Jurada Criadero en Web', 
        'Inscripción de lechigadas'
    ]
    
    # Obtener todos los trámites
    todos_tramites = list(Tramites.objects.all())
    
    # Ordenar según el orden específico
    tramites_ordenados = []
    for nombre_ordenado in orden_especifico:
        for tramite in todos_tramites:
            if tramite.nombre == nombre_ordenado:
                tramites_ordenados.append(tramite)
                break
    
    # Agregar cualquier trámite que no esté en la lista específica al final
    for tramite in todos_tramites:
        if tramite not in tramites_ordenados:
            tramites_ordenados.append(tramite)
    
    return render(request, 'tramites.html', {'tramites': tramites_ordenados})

def preguntas_frecuentes(request):
    # Obtener las categorías disponibles del modelo
    categorias = PreguntasFrecuentes.CATEGORIA_CHOICES
    
    return render(request, 'preguntas_frecuentes.html', {'categorias': categorias})

def detalle_preguntas_frecuentes(request, categoria):
    # Obtener el nombre legible de la categoría
    categoria_nombre = dict(PreguntasFrecuentes.CATEGORIA_CHOICES).get(categoria, categoria)
    
    # Obtener las preguntas de la categoría específica
    preguntas = PreguntasFrecuentes.objects.filter(categoria=categoria).order_by('orden')
    
    return render(request, 'detalle_preguntas_frecuentes.html', {
        'categoria': categoria,
        'categoria_nombre': categoria_nombre,
        'preguntas': preguntas
    })

def contacto(request):
    return render(request, 'contacto.html')

def test(request):
    """Vista de prueba que incluye diagnóstico de archivos estáticos"""
    # Información básica del sistema
    system_info = {
        'url_path': request.path,
        'method': request.method,
        'user': str(request.user),
    }
    
    # Información de archivos estáticos (con manejo de errores)
    static_info = {
        'STATIC_URL': '/static/',
        'STATIC_ROOT': 'No disponible',
        'STATIC_ROOT_EXISTS': False,
        'STATIC_ROOT_CONTENTS': [],
    }
    
    try:
        from django.conf import settings
        import os
        
        static_info['STATIC_URL'] = getattr(settings, 'STATIC_URL', '/static/')
        static_info['STATIC_ROOT'] = getattr(settings, 'STATIC_ROOT', 'No configurado')
        
        if static_info['STATIC_ROOT'] and static_info['STATIC_ROOT'] != 'No configurado':
            static_info['STATIC_ROOT_EXISTS'] = os.path.exists(static_info['STATIC_ROOT'])
            if static_info['STATIC_ROOT_EXISTS']:
                try:
                    static_info['STATIC_ROOT_CONTENTS'] = os.listdir(static_info['STATIC_ROOT'])
                except:
                    static_info['STATIC_ROOT_CONTENTS'] = ['Error al listar archivos']
    except Exception as e:
        static_info['STATIC_ROOT_CONTENTS'] = [f'Error: {str(e)}']
    
    return render(request, 'test.html', {
        'static_info': static_info,
        'system_info': system_info
    })