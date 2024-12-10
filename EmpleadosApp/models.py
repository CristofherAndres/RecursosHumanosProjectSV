from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    salario = models.FloatField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido
