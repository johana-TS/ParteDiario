from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.

class FechaRegistro(admin.ModelAdmin):
    readonly_fields=("ingresadoFecha",)


admin.site.register(agente)
admin.site.register(parteDiario,FechaRegistro)
admin.site.register(departamento)
