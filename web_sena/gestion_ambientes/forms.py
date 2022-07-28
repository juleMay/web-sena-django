from multiprocessing import context
from django.forms import ModelForm, TextInput, NumberInput, Select, ChoiceField

from .models import Ambiente


class AmbienteForm(ModelForm):
    class Meta:
        model = Ambiente
        fields = ['id', 'nombre', 'tipo', 'aforo', 'ubicacion']
        labels = {
            'id': "",
            "nombre":  "",
            'tipo':"Tipo de Ambiente",
            'aforo':"",
            'ubicacion':""
        }
        widgets = {
            'id': TextInput(attrs={'class': "form-control", 'placeholder': 'Id del Ambiente'}),
            'nombre': TextInput(attrs={'class': "form-control", 'placeholder': 'Nombre del Ambiente'}),
            'tipo': Select(attrs={'class': "form-control"}),
            'aforo': NumberInput(attrs={'class': "form-control", 'placeholder': 'Capacidad Estudiantes'}),
            'ubicacion': TextInput(attrs={'class': "form-control", 'placeholder': 'Ubicación del Ambiente'})
        }
