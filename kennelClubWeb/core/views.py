from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Noticias, Juez, TipoJuez, Evento, Ranking, Reglamentos, Crianza, HistoriaRazas, FotoHistoriaRaza, Tramites, PreguntasFrecuentes
from datetime import datetime, timedelta
import re

# Create your views here.
def home(request):
    ultimas_noticias = Noticias.objects.all().order_by('-fecha')[:3]
    return render(request, 'home.html', {'ultimas_noticias': ultimas_noticias})

def sitemap_xml(request):
    """Genera un sitemap XML dinámico"""
    # URLs estáticas principales
    static_urls = [
        {'url': '/', 'priority': '1.0', 'changefreq': 'daily'},
        {'url': '/noticias/', 'priority': '0.8', 'changefreq': 'daily'},
        {'url': '/eventos/', 'priority': '0.8', 'changefreq': 'weekly'},
        {'url': '/jueces-nacionales/', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/rankings/', 'priority': '0.8', 'changefreq': 'weekly'},
        {'url': '/historia-razas/', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/crianza/', 'priority': '0.7', 'changefreq': 'monthly'},
        {'url': '/tramites/', 'priority': '0.6', 'changefreq': 'monthly'},
        {'url': '/reglamentos/', 'priority': '0.6', 'changefreq': 'monthly'},
        {'url': '/preguntas-frecuentes/', 'priority': '0.6', 'changefreq': 'monthly'},
        {'url': '/quienes-somos/', 'priority': '0.5', 'changefreq': 'yearly'},
        {'url': '/contacto/', 'priority': '0.5', 'changefreq': 'yearly'},
    ]
    
    # URLs dinámicas de noticias
    noticias = Noticias.objects.all().order_by('-fecha')
    noticia_urls = []
    for noticia in noticias:
        noticia_urls.append({
            'url': f'/noticias/{noticia.id}/',
            'priority': '0.6',
            'changefreq': 'monthly',
            'lastmod': noticia.fecha.strftime('%Y-%m-%d')
        })
    
    # URLs dinámicas de historias de razas
    historias = HistoriaRazas.objects.all()
    historia_urls = []
    for historia in historias:
        historia_urls.append({
            'url': f'/historia-razas/{historia.id}/',
            'priority': '0.5',
            'changefreq': 'yearly'
        })
    
    context = {
        'static_urls': static_urls,
        'noticia_urls': noticia_urls,
        'historia_urls': historia_urls,
        'base_url': request.build_absolute_uri('/').rstrip('/')
    }
    
    xml_content = render_to_string('sitemap.xml', context)
    return HttpResponse(xml_content, content_type='application/xml')

def robots_txt(request):
    robots_content = render_to_string('robots.txt')
    return HttpResponse(robots_content, content_type='text/plain')

def noticias(request):
    # Obtener todas las noticias ordenadas por fecha
    noticias_list = Noticias.objects.all().order_by('-fecha')
    
    # Configurar paginación - 4 noticias por página (1 noticia por fila en móvil)
    paginator = Paginator(noticias_list, 4)
    
    # Obtener el número de página de los parámetros GET
    page = request.GET.get('page')
    
    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número, mostrar la primera página
        noticias = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango, mostrar la última página
        noticias = paginator.page(paginator.num_pages)
    
    return render(request, 'noticias.html', {
        'noticias': noticias,
        'paginator': paginator
    })

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
        if jueces.exists():
            jueces_por_tipo[tipo] = jueces
    
    return render(request, 'jueces_nacionales.html', {
        'jueces_por_tipo': jueces_por_tipo,
        'tipos_juez': tipos_juez
    })

def eventos(request):
    año_filtro = request.GET.get('año')
    mes_filtro = request.GET.get('mes')
    
    # Obtener todos los eventos
    eventos_list = Evento.objects.all().order_by('-fecha_inicio')
    
    # Aplicar filtros
    if año_filtro:
        eventos_list = eventos_list.filter(fecha_inicio__year=año_filtro)
    
    if mes_filtro:
        eventos_list = eventos_list.filter(fecha_inicio__month=mes_filtro)
    
    # Configurar paginación - 6 eventos por página
    paginator = Paginator(eventos_list, 6)
    
    # Obtener el número de página de los parámetros GET
    page = request.GET.get('page')
    
    try:
        eventos = paginator.page(page)
    except PageNotAnInteger:
        eventos = paginator.page(1)
    except EmptyPage:
        eventos = paginator.page(paginator.num_pages)
    
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
        fecha_actual = evento.fecha_inicio
        fecha_fin = evento.fecha_termino
        
        # Verificar que las fechas sean válidas
        if fecha_actual and fecha_fin and fecha_actual <= fecha_fin:
            while fecha_actual <= fecha_fin:
                evento.dias_lista.append(fecha_actual)
                fecha_actual += timedelta(days=1)
        
        evento.dias_formateados = []
        for fecha in evento.dias_lista:
            dia_num = fecha.day
            mes_nombre = meses_es[fecha.month]
            evento.dias_formateados.append(f"{dia_num} {mes_nombre}")
    
    return render(request, 'eventos.html', {
        'eventos': eventos,
        'paginator': paginator,
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
    rankings = Ranking.objects.all().order_by('-fecha')
    
    rankings_por_año = {}
    años_disponibles = []
    
    for ranking in rankings:
        año = ranking.fecha.split('-')[0]
        
        if año not in rankings_por_año:
            rankings_por_año[año] = []
            años_disponibles.append(año)
        
        rankings_por_año[año].append(ranking)
    
    años_disponibles.sort(reverse=True)
    
    return render(request, 'rankings.html', {
        'rankings_por_año': rankings_por_año,
        'años_disponibles': años_disponibles,
        'rankings': rankings
    })

def reglamentos(request):
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
    orden_especifico = [
        'Trámites a distancia',
        'Obtención de Kennel Name, afijo o nombre de criadero, Declaración Jurada Criadero en Web', 
        'Inscripción de lechigadas'
    ]
    
    todos_tramites = list(Tramites.objects.all())
    
    tramites_ordenados = []
    for nombre_ordenado in orden_especifico:
        for tramite in todos_tramites:
            if tramite.nombre == nombre_ordenado:
                tramites_ordenados.append(tramite)
                break
    
    for tramite in todos_tramites:
        if tramite not in tramites_ordenados:
            tramites_ordenados.append(tramite)
    
    return render(request, 'tramites.html', {'tramites': tramites_ordenados})

def preguntas_frecuentes(request):
    categorias = PreguntasFrecuentes.CATEGORIA_CHOICES
    
    return render(request, 'preguntas_frecuentes.html', {'categorias': categorias})

def detalle_preguntas_frecuentes(request, categoria):
    categoria_nombre = dict(PreguntasFrecuentes.CATEGORIA_CHOICES).get(categoria, categoria)
    
    preguntas = PreguntasFrecuentes.objects.filter(categoria=categoria).order_by('orden')
    
    return render(request, 'detalle_preguntas_frecuentes.html', {
        'categoria': categoria,
        'categoria_nombre': categoria_nombre,
        'preguntas': preguntas
         })

def contacto(request):
    if request.method == 'POST':
        try:
            from django.core.mail import send_mail
            
            nombre = request.POST.get('nombre', '').strip()
            email = request.POST.get('email', '').strip()
            asunto = request.POST.get('asunto', '').strip()
            mensaje = request.POST.get('mensaje', '').strip()
            
            field_errors = {}
            
            if not nombre:
                field_errors['nombre'] = 'El nombre es obligatorio'
            elif len(nombre) < 2:
                field_errors['nombre'] = 'El nombre debe tener al menos 2 caracteres'
            
            if not email:
                field_errors['email'] = 'El email es obligatorio'
            else:
                email_validator = EmailValidator()
                try:
                    email_validator(email)
                except ValidationError:
                    field_errors['email'] = 'Formato de email inválido'
                
                email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(email_pattern, email):
                    field_errors['email'] = 'Formato de email inválido'
                
                domain = email.split('@')[1].lower()
                temp_domains = ['10minutemail.com', 'tempmail.org', 'guerrillamail.com', 'mailinator.com']
                if domain in temp_domains:
                    field_errors['email'] = 'No se permiten emails temporales'
            
            if not asunto:
                field_errors['asunto'] = 'El asunto es obligatorio'
            elif len(asunto) < 5:
                field_errors['asunto'] = 'El asunto debe tener al menos 5 caracteres'
            
            if not mensaje:
                field_errors['mensaje'] = 'El mensaje es obligatorio'
            elif len(mensaje) < 10:
                field_errors['mensaje'] = 'El mensaje debe tener al menos 10 caracteres'
            
            if field_errors:
                return JsonResponse({
                    'success': False,
                    'message': 'Por favor, corrige los errores en el formulario',
                    'field_errors': field_errors
                }, status=400)
            
            # Contenido del correo
            email_content = f"""
Nuevo mensaje de contacto desde el sitio web Kennel Club de Chile

Nombre: {nombre}
Email: {email}
Asunto: {asunto}

Mensaje:
{mensaje}

---
Este mensaje fue enviado desde el formulario de contacto del sitio web.
            """
            send_mail(
                subject=f'Nuevo mensaje de contacto: {asunto}',
                message=email_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            return JsonResponse({
                'success': True,
                'message': '¡Mensaje enviado exitosamente! Nos pondremos en contacto contigo pronto.'
            }, status=200)
            
        except Exception as e:
            print(f"ERROR EN FORMULARIO DE CONTACTO: {e}")
            print(f"Tipo de error: {type(e).__name__}")
            
            return JsonResponse({
                'success': False,
                'message': f'Error al enviar mensaje: {str(e)}'
            }, status=500)
    
    return render(request, 'contacto.html')

def validacion_username(username):
    # Valida que el username no contenga patrones peligrosos
    
    if not username:
        return False, "El nombre de usuario no puede estar vacío"
    
    # Convertir a minúsculas para comparaciones
    username_lower = username.lower()
    
    # Patrones peligrosos de inyección SQL
    sql_patterns = [
        'drop', 'delete', 'insert', 'update', 'select', 'union', 'exec', 'execute',
        'script', 'javascript', 'vbscript', 'onload', 'onerror', 'onclick',
        '--', '/*', '*/', 'xp_', 'sp_', 'sysobjects', 'syscolumns',
        'information_schema', 'master..', 'temp..', 'char(', 'nchar(',
        'varchar(', 'nvarchar(', 'convert(', 'cast(', 'declare', 'begin',
        'end', 'if', 'else', 'case', 'when', 'then', 'while', 'for',
        'break', 'continue', 'return', 'goto', 'waitfor', 'delay',
        'backup', 'restore', 'shutdown', 'kill', 'dbcc', 'reconfigure'
    ]
    
    # Patrones de comandos del sistema
    system_patterns = [
        'cmd', 'powershell', 'bash', 'sh', 'net', 'ipconfig', 'ping',
        'tracert', 'nslookup', 'telnet', 'ftp', 'ssh', 'scp', 'wget',
        'curl', 'nc', 'netcat', 'nmap', 'dir', 'ls', 'cat', 'type',
        'echo', 'set', 'env', 'system', 'shell', 'terminal', 'console'
    ]
    
    # Patrones de archivos peligrosos
    file_patterns = [
        '..', '\\', '//', '~', 'root', 'home', 'etc', 'var', 'tmp',
        'temp', 'windows', 'system32', 'program files', 'users',
        '.exe', '.bat', '.cmd', '.ps1', '.sh', '.py', '.php', '.js',
        '.vbs', '.jar', '.war', '.ear', '.dll', '.so', '.dylib'
    ]
    
    # Patrones de caracteres especiales peligrosos
    dangerous_chars = ['<', '>', '"', "'", '&', '|', ';', '`', '$', '{', '}', '[', ']']
    
    # Verificar patrones SQL
    for pattern in sql_patterns:
        if pattern in username_lower:
            return False, f"Ingrese un Nombre de usuario válido"
    
    # Verificar patrones del sistema
    for pattern in system_patterns:
        if pattern in username_lower:
            return False, f"Ingrese un Nombre de usuario válido"
    
    # Verificar patrones de archivos
    for pattern in file_patterns:
        if pattern in username_lower:
            return False, f"Ingrese un Nombre de usuario válido"
    
    # Verificar caracteres peligrosos
    for char in dangerous_chars:
        if char in username:
            return False, f"Ingrese un Nombre de usuario válido"
    
    # Verificar longitud mínima y máxima
    if len(username) < 3:
        return False, "El Nombre de usuario debe tener al menos 3 caracteres"
    
    if len(username) > 30:
        return False, "El Nombre de usuario no puede exceder 30 caracteres"
    
    # Verificar que solo contenga caracteres alfanuméricos, guiones y guiones bajos
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False, "El Nombre de usuario solo puede contener letras, números, guiones y guiones bajos"
    
    # Verificar que no empiece o termine con caracteres especiales
    if username.startswith(('-', '_')) or username.endswith(('-', '_')):
        return False, "El Nombre de usuario no puede empezar o terminar con guiones o guiones bajos"
    
    return True, "Nombre de usuario válido"

def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validar seguridad del username
        is_valid, validation_message = validacion_username(username)
        if not is_valid:
            error = validation_message
            return render(request, 'login.html', {'error': error})
        
        # Continuar con la autenticación
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Nombre de usuario o contraseña incorrectos.'
    
    return render(request, 'login.html', {'error': error})

def error(request):
    return render(request, 'error.html')