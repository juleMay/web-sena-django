from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Programa)
admin.site.register(Competencia)
admin.site.register(Docente)
admin.site.register(Horario)