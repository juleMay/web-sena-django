from multiprocessing import context
from django.forms import ModelForm, DateTimeInput, Select

from .models import Horario
    

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['ambiente', 'competencia', 'docente']
        labels = {
            'ambiente': "Ambiente",
            "competencia": "Competencia",
            'docente': "Docente",
        }
        widgets = {
            'ambiente': Select(attrs={'class': "form-control"}),
            'competencia': Select(attrs={'class': "form-control"}),
            'docente': Select(attrs={'class': "form-control"}),
        }
