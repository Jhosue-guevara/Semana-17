from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Edad = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.nombre} {self.Apellido}'
class Area(models.Model):
    Nombre_del_Area = models.CharField(max_length=60)
    Descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Nombre_del_Area

class empleado(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Edad = models.PositiveIntegerField()
    Areaid = models.ForeignKey(Area,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"
class Ventas(models.Model):
    Fecha = models.DateTimeField()
    Monto = models.FloatField()
    Clienteid = models.ForeignKey(cliente,on_delete=models.CASCADE)
    Empleadoid = models.ForeignKey(empleado,on_delete=models.CASCADE)