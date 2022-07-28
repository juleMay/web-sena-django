from django.shortcuts import render

# Create your views here.
from gestion_horarios.models import Docente

def home(request):
    return render(request, 'HomeTemplate.html')

def horario(request):
    docente = Docente.objects.get(nombre="Juan Perez")
    horario = list(docente.horario_set.all())
    print(horario)
    return render(request, 'HorarioTemplate.html', {'horario':horario})