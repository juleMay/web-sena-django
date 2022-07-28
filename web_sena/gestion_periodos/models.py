from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
# Create your models here.


class Periodo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    def save(self, *args, **kwargs):
        if self.fecha_final != self.fecha_inicio + timedelta(days=90) and self.fecha_final != self.fecha_inicio + timedelta(days=180):
            raise ValidationError(
                "Ingrese una fecha final válida. El periodo debe durar 3 o 6 meses")
        super(Periodo, self).save(*args, **kwargs)

    def __str__(self):
        return "ID: {0} | NOMBRE: {1} | FECHA DE INICIO: {2} | FECHA FINAL: {3}".format(self.pk, self.nombre, self.fecha_inicio, self.fecha_final)
