from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UserAuthentication.decorators import allowed_users

# Create your views here.
from gestion_horarios.models import Docente

def home(request):
    return render(request, 'HomeTemplate.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['profesor'])
def horario(request):
    username = request.user.username
    docente = Docente.objects.get(username=username)
    horario = docente.horario_set.all()
    field_names = ["Ambiente", "Competencia", "Día", "Hora Inicial", "Hora Final"]
    values = horario.values('ambiente__nombre', 'competencia__nombre', 'dia', 'hora_inicio', 'hora_final')
    return render(request, 'HorarioTemplate.html', {'labels':field_names,'horario':values})

@login_required(login_url='login')
@allowed_users(allowed_roles=['profesor'])
def perfil(request):
    username = request.user.username
    docente = Docente.objects.filter(username=username)
    field_names = ["Nombre", "Identificación", "Nivel", "Contrato", "Area"]
    values = docente.values('nombre', 'identificación', 'tipo_docente', 'tipo_contrato', 'area').first
    return render(request, 'PerfilTemplate.html', {'labels':field_names,'profesor':values})