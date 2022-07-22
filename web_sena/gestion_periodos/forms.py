from multiprocessing import context
from django.forms import ModelForm, TextInput, DateTimeInput, ClearableFileInput, Textarea

from .models import Periodo


class PeriodoForm(ModelForm):
    class Meta:
        model = Periodo
        fields = ['nombre', 'fecha_inicio', 'fecha_final']
        widgets = {
            'nombre': TextInput(attrs={'class': "form-control", 'placeholder': 'Nombre del Producto'}),
            'fecha_inicio': DateTimeInput(attrs={'class': "form-control",'type': "date"}),
            'fecha_final': DateTimeInput(attrs={'class': "form-control",'type': "date"}),
        }
