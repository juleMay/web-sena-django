from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Ambiente(models.Model):
    def validate_positive(value):
        if value <= 0:
            raise ValidationError(
                _('Ingrese un número válido. %(value)s no es un número positivo'),
                params={'value': value},
            )
            
    TIPO = (
        ('virtual', 'Virtual'),
        ('presencial', 'Presencial'),
    )

    id = models.CharField(max_length=64, primary_key=True)
    nombre = models.CharField(max_length=200,unique=True)
    tipo = models.CharField(max_length=200, choices=TIPO)
    aforo = models.IntegerField(validators=[validate_positive])
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return "ID: {0} | NOMBRE: {1} | TIPO: {2} | CAPACIDAD ESTUDIANTES: {3} | UBICACION: {4}".format(self.pk, self.nombre, self.tipo, self.aforo, self.ubicacion)
