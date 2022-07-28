from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from UserAuthentication.decorators import allowed_users

# Create your views here.

from .models import Periodo
from .forms import PeriodoForm

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def home(request):
    periodos = Periodo.objects.all()
    field_names = ["Id","Nombre","Fecha de Inicio","Fecha Final"]
    values = periodos.values()
    return render(request, 'CrudTemplate.html', {"field_names": field_names, 'values': values})

@login_required(login_url='login')
def addPeriodo(request):
    form = PeriodoForm()
    if request.method == 'POST':
        form = PeriodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('periodos')

    return render(request, 'AddTemplate.html', {'form': form, 'nombre_crud': "Periodo Académico"})

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def updatePeriodo(request, id):
    periodo = Periodo.objects.get(id=id)
    form = PeriodoForm(instance=periodo)
    if request.method == 'POST':
        form = PeriodoForm(request.POST, instance=periodo)
        if form.is_valid():
            form.save()
            return redirect('periodos')
    return render(request, 'AddTemplate.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador','coordinador'])
def deletePeriodo(request, id):
    periodo = Periodo.objects.get(id=id)
    periodo.delete()
    return redirect('periodos')
