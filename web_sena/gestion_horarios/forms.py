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
            'hora_inicio': TimeInput(attrs={'class': "form-control", 'type':"time"}),
            'hora_final': TimeInput(attrs={'class': "form-control", 'type':"time"}),
        }
        
    def clean(self):
        super(HorarioForm, self).clean()

        ambiente = self.cleaned_data.get('ambiente')
        dia = self.cleaned_data.get('dia')
        hora_inicio = self.cleaned_data.get('hora_inicio')
        hora_inicio = hora_inicio.replace(minute=(hora_inicio.minute+1) % 24)
        hora_final = self.cleaned_data.get('hora_final')
        hora_final = hora_final.replace(minute=(hora_final.minute-1) % 24)
        

        ambientes = Horario.objects.filter(ambiente=ambiente, dia=dia, hora_inicio__range=(hora_inicio, hora_final), hora_final__range=(hora_inicio, hora_final))
        if ambientes:
            self._errors['hora_final'] = self.error_class([
                'Ingrese una franja horaria válida. Esta franja horaria está ocupada'])

        return self.cleaned_data
