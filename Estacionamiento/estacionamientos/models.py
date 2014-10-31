from django.db import models

# Create your models here.

class Estacionamiento(models.Model):
    Nombre = models.CharField(max_length=200)
    RIF = models.CharField(max_length=10)
    Encargado = models.CharField(max_length=100)
    Telefono_1 = models.IntegerField()
    Telefono_2 = models.IntegerField()
    Telefono_3 = models.IntegerField()
    Correo_1 = models.EmailField(max_length=100)
    Correo_2 = models.EmailField(max_length=100)
    Puestos = models.IntegerField(default=0)
    def __str__(self):
        return u'%d %s' % (self.id, self.Nombre)

class Puesto(models.Model):
    Estacionamiento = models.ForeignKey(Estacionamiento)
    ocupado = models.BooleanField(default=False)
    def __str__(self):
        return u'%d %s' % (self.id, self.ocupado)
