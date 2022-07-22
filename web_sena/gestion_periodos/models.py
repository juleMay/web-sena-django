from django.db import models

# Create your models here.

class Periodo(models.Model):
    DURACION = (
        ('3', '3 Meses'),
        ('6', '6 Meses'),
    )

    nombre = models.CharField(max_length=200)
    duracion = models.CharField(max_length=200, choices=DURACION)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()

    def __str__(self):
        return "NOMBRE:{0} DURACION:{1} FECHA DE INICIO:{2} FECHA FINAL:{3}".format(self.nombre, self.duracion, self.fecha_inicio, self.fecha_final)
