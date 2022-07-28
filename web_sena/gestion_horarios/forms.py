from multiprocessing import context
from django.forms import ModelForm, DateTimeInput, Select

from .models import Horario
    

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['ambiente', 'competencia', 'docente', 'inicio']
        labels = {
            'ambiente': "Ambiente",
            "competencia": "Competencia",
            'docente': "Docente",
            'inicio': "Fecha y Hora de Inicio",
        }
        widgets = {
            'ambiente': Select(attrs={'class': "form-control"}),
            'competencia': Select(attrs={'class': "form-control"}),
            'docente': Select(attrs={'class': "form-control"}),
            'inicio': DateTimeInput(attrs={'class': "form-control",'type': "date"}),
        }
