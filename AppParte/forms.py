from dataclasses import fields
from django.forms import ModelForm
from .models import parteDiario


class parteDiarioClass(ModelForm):
    class Meta:
        model=parteDiario
        fields= ['agenteParte',
                 'detalle',
                 'cargaFecha',
                 ]
