from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from UserAuthentication.decorators import allowed_users

# Create your views here.

from .models import Ambiente
from .forms import AmbienteForm

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def home(request):
    ambientes = Ambiente.objects.all()
    field_names = ["Id","Nombre","Tipo","Capacidad","Ubicación"]
    values = ambientes.values()
    return render(request, 'CrudTemplate.html', {"field_names": field_names, 'values': values, 'root':'ambientes'})

@login_required(login_url='login')
def addAmbiente(request):
    form = AmbienteForm()
    if request.method == 'POST':
        form = AmbienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ambientes')
    return render(request, 'AddTemplate.html', {'form': form, 'nombre_crud': "Ambiente Académico", 'root':'ambientes'})

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def updateAmbiente(request, id):
    periodo = Ambiente.objects.get(id=id)
    form = AmbienteForm(instance=periodo)
    if request.method == 'POST':
        form = AmbienteForm(request.POST, instance=periodo)
        if form.is_valid():
            form.save()
            return redirect('ambientes')
    return render(request, 'AddTemplate.html', {'form': form, 'root':'ambientes'})

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def deleteAmbiente(request, id):
    periodo = Ambiente.objects.get(id=id)
    periodo.delete()
    return redirect('ambientes')
