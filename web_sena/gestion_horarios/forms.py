from multiprocessing import context
from django.forms import ModelForm, TextInput, DateTimeInput, Select, DurationField

from .models import Horario


from django.forms.widgets import TextInput
from django.utils.dateparse import parse_duration

class DurationInput(TextInput):

    def _format_value(self, value):
        duration = parse_duration(value)

        seconds = duration.seconds

        minutes = seconds // 60
        seconds = seconds % 60
        
        hours = minutes // 60
        minutes = minutes % 60
        
        return '{:02d}'.format(hours)
    

class HorarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = ['ambiente', 'competencia', 'docente', 'inicio', 'duracion']
        labels = {
            'ambiente': "Ambiente",
            "competencia": "Competencia",
            'docente': "Docente",
            'inicio': "Fecha y Hora de Inicio",
            'duracion': "Duración"
        }
        widgets = {
            'ambiente': Select(attrs={'class': "form-control"}),
            'competencia': Select(attrs={'class': "form-control"}),
            'docente': Select(attrs={'class': "form-control"}),
            'inicio': DateTimeInput(attrs={'class': "form-control",'type': "date"}),
            'duracion': DurationInput(attrs={'class': "form-control"})
        }
