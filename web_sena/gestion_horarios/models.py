from django.db import models

# Create your models here.

class Horario(models.Model):
    TIPO = (
        ('virtual', 'Virtual'),
        ('presencial', 'Presencial'),
    )
    
    id = models.CharField(max_length=64, primary_key=True)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200, choices=TIPO)
    aforo = models.IntegerField()
    ubicacion = models.CharField(max_length=200)
    
    def __str__(self):
        return "NOMBRE: {0} | TIPO: {1} | CAPACIDAD ESTUDIANTES: {2} | UBICACION: {3}".format(self.nombre, self.tipo, self.aforo, self.ubicacion)
    
    
    create table HORARIO
(
   AMBIENTE_ID          varchar(6) not null,
   COMPETENCIA_ID       numeric(8,0) not null,
   DOCENTE_ID           int not null,
   HORARIO_DIA          varchar(10),
   HORARIO_HORA_INICIO  numeric(8,0),
   HORARIO_HORA_FIN     numeric(8,0),
   HORARIO_DURACION     numeric(8,0),
   primary key (AMBIENTE_ID, COMPETENCIA_ID, DOCENTE_ID)
);
