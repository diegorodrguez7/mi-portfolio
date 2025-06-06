from django.shortcuts import render
from .models import Proyecto, Habilidad, Resumen, Servicio, EntradaBlog # Asegúrate de que el modelo esté importado

def inicio(request):
    proyectos = Proyecto.objects.all().order_by('-id')  # O usa .order_by('-fecha_creacion') si tienes esa columna
    habilidades = Habilidad.objects.all().order_by('-nivel')
    resumen = Resumen.objects.first()
    servicios = Servicio.objects.all()
    return render(request, 'proyectos/index.html', {
        'proyectos': proyectos,
        'habilidades': habilidades,
        'resumen': resumen,
        'servicios': servicios
    })

def blog(request):
    entradas = EntradaBlog.objects.all().order_by('-fecha_creacion')
    return render(request, 'proyectos/blog.html', {'entradas': entradas})


