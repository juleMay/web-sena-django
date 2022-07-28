from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from UserAuthentication.decorators import allowed_users

# Create your views here.

from .models import Horario
from .forms import HorarioForm

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def home(request):
    horarios = Horario.objects.all()
    field_names = ["Id","Nombre","Tipo","Capacidad","Ubicación"]
    values = horarios.values()
    return render(request, 'CrudTemplate.html', {"field_names": field_names, 'values': values, 'root':'horarios'})

@login_required(login_url='login')
def addHorario(request):
    form = HorarioForm()
    if request.method == 'POST':
        form = HorarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('horarios')
    return render(request, 'AddTemplate.html', {'form': form, 'nombre_crud': "Horario", 'root':'horarios'})

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def updateHorario(request, id):
    periodo = Horario.objects.get(id=id)
    form = HorarioForm(instance=periodo)
    if request.method == 'POST':
        form = HorarioForm(request.POST, instance=periodo)
        if form.is_valid():
            form.save()
            return redirect('horarios')
    return render(request, 'AddTemplate.html', {'form': form, 'root':'horarios'})

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def deleteHorario(request, id):
    periodo = Horario.objects.get(id=id)
    periodo.delete()
    return redirect('horarios')