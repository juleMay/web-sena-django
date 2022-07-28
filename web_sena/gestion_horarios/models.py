from django.db import models

# Create your models here.
from gestion_ambientes.models import Ambiente


class Programa(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "ID: {0} | NOMBRE: {1}".format(self.pk, self.nombre)


class Competencia(models.Model):
    TIPO = (
        ('generica', 'Genérica'),
        ('especifica', 'Específica'),
    )
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200, choices=TIPO)
    programa = models.ForeignKey(
        Programa, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "ID: {0} | NOMBRE: {1} | TIPO: {2} | PROGRAMA: {3}".format(self.pk, self.nombre, self.tipo, self.programa.nombre)


class Docente(models.Model):
    TIPO_IDENTIFICACION = (
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
    )
    TIPO_DOCENTE = (
        ('tecnico', 'Técnico'),
        ('profesional', 'Profesional'),
    )
    TIPO_CONTRATO = (
        ('PT', 'Planta'),
        ('CNT', 'Contratista'),
    )
    nombre = models.CharField(max_length=200)
    tipo_identificación = models.CharField(
        max_length=200, choices=TIPO_IDENTIFICACION)
    identificación = models.CharField(max_length=64)
    tipo_docente = models.CharField(max_length=200, choices=TIPO_DOCENTE)
    tipo_contrato = models.CharField(max_length=200, choices=TIPO_CONTRATO)
    area = models.CharField(max_length=200)


class Horario(models.Model):
    ambiente = models.ForeignKey(
        Ambiente, null=True, on_delete=models.SET_NULL)
    competencia = models.ForeignKey(
        Competencia, null=True, on_delete=models.SET_NULL)
    docente = models.ForeignKey(Docente, null=True, on_delete=models.SET_NULL)

    inicio = models.DateTimeField()
    duracion = models.DurationField()

    def __str__(self):
        return "ID: {0} | NOMBRE: {1} | TIPO: {2} | CAPACIDAD ESTUDIANTES: {3} | UBICACION: {4}".format(self.pk, self.ambiente.nombre, self.competencia.nombre, self.docente.nombre, self.inicio, self.duracion)