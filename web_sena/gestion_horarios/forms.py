from multiprocessing import context
from django.forms import ModelForm, TimeInput, Select

from .models import Horario
    

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['ambiente', 'competencia', 'docente', 'dia', 'hora_inicio', 'hora_final']
        labels = {
            'ambiente': "Ambiente",
            "competencia": "Competencia",
            'docente': "Docente",
            'dia': "Día",
            'hora_inicio': "Hora Inicial",
            'hora_final': "Hora Final"
        }
        widgets = {
            'ambiente': Select(attrs={'class': "form-control"}),
            'competencia': Select(attrs={'class': "form-control"}),
            'docente': Select(attrs={'class': "form-control"}),
            'dia': Select(attrs={'class': "form-control"}),
            'hora_inicio': TimeInput(attrs={'class': "form-control"}),
            'hora_final': TimeInput(attrs={'class': "form-control"}),
        }
