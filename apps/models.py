from django.db import models

# Crear la clase empleado.
class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=50)
    fecha=models.DateField()
    sueldo=models.FloatField()

    def __str__(self):
        return self.nombre




