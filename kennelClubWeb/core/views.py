from django.shortcuts import render, get_object_or_404
from .models import Noticias

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
    return render(request, 'crianza.html')