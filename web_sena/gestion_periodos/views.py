from django.shortcuts import render

# Create your views here.

from .models import Periodo
from .forms import PeriodoForm


def home(request):
    periodos = Periodo.objects.all()
    return render(request, 'CrudTemplate.html', {'crud': periodos})


def addPeriodo(request):
    form = PeriodoForm()
    if request.method == 'POST':
        form = PeriodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('periodos')

    return render(request, 'AddTemplate.html', {'form': form})


def updatePeriodo(request, id):
    periodo = Periodo.objects.get(id=id)
    form = PeriodoForm(instance=periodo)
    if request.method == 'POST':
        form = PeriodoForm(request.POST, instance=periodo)
        if form.is_valid():
            form.save()
            return redirect('crud')
    return render(request, 'AddTemplate.html', {'form': form})


def deletePeriodo(request, id):
    periodo = Periodo.objects.get(id=id)
    periodo.delete()
    return redirect('home')
