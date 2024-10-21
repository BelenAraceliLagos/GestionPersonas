from typing import Any
from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    cargo = models.CharField(max_length=100, verbose_name='cargo')
    departamento = models.CharField(max_length=100, verbose_name='depto')
    salario = models.IntegerField(max_length=100, verbose_name='salario')
    fecha = models.DateField(verbose_name='fecha', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Cargo: " + self.cargo
        return fila
    
    
    