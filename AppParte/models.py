from email.policy import default
from random import choices
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class departamento(models.Model):
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class agente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    dto_agente= models.ForeignKey(departamento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    


class parteDiario(models.Model):
    opcion = (
        ("P","Presente"),
        ("LAO","Licencia Anual Ordinaria"),
        ("LE","Licencia por Enfermedad"),
        ("LM","Licencia por Maternidad"),
        ("Art","Articulo"),
        ("A","Ausente"),
        
    )
    detalle = models.CharField(choices=opcion, 
                               max_length=35,
                                 default= "Presente")
    ingresadoFecha= models.DateTimeField(auto_now_add=True)
    usuarioIngreso=models.ForeignKey(User, on_delete= models.CASCADE)
    visadoFecha=models.DateTimeField(null=True)
    cargaFecha=models.DateTimeField(null=True, blank=True)
    usuarioVisado=models.CharField(max_length=4, null=True)
    estado= models.BooleanField(default=True)
    agenteParte= models.ForeignKey(agente, on_delete=models.CASCADE, null=True)
    


    def __str__(self):
        return  str(self.agenteParte) + ' - ' + str(self.ingresadoFecha) + ' - ' + self.detalle