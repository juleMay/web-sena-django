from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UserAuthentication.decorators import allowed_users

# Create your views here.
from gestion_horarios.models import Docente

@login_required(login_url='login')
@allowed_users(allowed_roles=['profesor'])
def home(request):
    return render(request, 'HomeTemplate.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['profesor'])
def horario(request):
    docente = Docente.objects.get(nombre="Juan Perez")
    horario = list(docente.horario_set.all())
    return render(request, 'HorarioTemplate.html', {'horario':horario})

@login_required(login_url='login')
@allowed_users(allowed_roles=['profesor'])
def perfil(request):
    docente = Docente.objects.get(nombre="Juan Perez")
    return render(request, 'PerfilTemplate.html', {'perfil':docente})