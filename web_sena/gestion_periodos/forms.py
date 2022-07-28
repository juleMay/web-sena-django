from multiprocessing import context
from django.forms import ModelForm, TextInput, DateInput
from .models import Periodo
from datetime import datetime, timedelta

class PeriodoForm(ModelForm):
    class Meta:
        model = Periodo
        fields = ['nombre', 'fecha_inicio', 'fecha_final']
        labels = {
            "nombre":  "",
            "fecha_inicio": "Fecha de Inicio",
            "fecha_final": "Fecha Final"
        }
        widgets = {
            'nombre': TextInput(attrs={'class': "form-control", 'placeholder': 'Nombre del Periodo'}),
            'fecha_inicio': DateInput(attrs={'class': "form-control", 'type': "date"}),
            'fecha_final': DateInput(attrs={'class': "form-control", 'type': "date"})
        }

    def clean(self):
        super(PeriodoForm, self).clean()

        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_final = self.cleaned_data.get('fecha_final')
        
        if fecha_final != (fecha_inicio + timedelta(days=90)) and fecha_final != (fecha_inicio + timedelta(days=180)):
            self._errors['fecha_final'] = self.error_class([
                'Ingrese una fecha final válida. El periodo debe durar 3 o 6 meses'])

        return self.cleaned_data
