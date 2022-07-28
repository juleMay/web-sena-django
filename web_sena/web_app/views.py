from django.shortcuts import render

# Create your views here.
from gestion_horarios.models import Docente

def home(request):
    return render(request, 'HomeTemplate.html')

def horario(request):
    profesor = Docente.objects.get(nombre="Juan Perez")
    cart = list(client.cart_set.all())
    horario = profe
    return render(request, 'HorarioTemplate.html')