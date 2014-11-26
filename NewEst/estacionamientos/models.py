# coding= utf-8
from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import RegexValidator
#from django import forms

# Create your models here.

class Estacionamiento(models.Model):
	propietario = models.CharField(max_length=64,null = False, blank = False, 
		validators=[RegexValidator
			#(regex='^( |[ñÑáéíóúÁÉÍÓÚa-zA-Z])*$',
			(regex='^([ a-zA-Z])*$',
			message="No puede contener numeros,'Ñ', ni caracteres acentuados"),
		]
	)
	nombre_est = models.CharField(max_length=64,null = False, blank = False)
	dir_est = models.CharField(max_length=256,null = False, blank = False)
	telf1 = models.CharField(max_length=12,null=False, blank=False, 
		validators=[RegexValidator
			(regex='^0(212|4(1(2|4|6)|2(4|6)))-?[1-9][0-9][0-9][0-9][0-9][0-9][0-9]$',
			message="Debe ser un telefono de ccs o de celular. Por Ejemplo: 0212-1234567"),
		]
	)
	telf2 = models.CharField(max_length=12,null=False,blank=True,
		validators=[RegexValidator
			(regex='^0(212|4(1(2|4|6)|2(4|6)))-?[1-9][0-9][0-9][0-9][0-9][0-9][0-9]$',
			message="Debe ser un telefono de ccs o de celular. Por Ejemplo: 0212-1234567"),
		]
	)
	telf3 = models.CharField(max_length=12,null=True,blank=True,
		validators=[RegexValidator
			(regex='^0(212|4(1(2|4|6)|2(4|6)))-?[1-9][0-9][0-9][0-9][0-9][0-9][0-9]$',
			message="Debe ser un telefono de ccs o de celular. Por Ejemplo: 0212-1234567"),
		]
	)
	email1 = models.EmailField()
	email2 = models.EmailField(blank=True)
	rif = models.CharField(max_length=12,null = False, blank = False,
		validators=[RegexValidator
			(regex='^(j|J|v|V|e|E|g|G|p|P)-?[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-?[0-9]$',
			message="Debe ser un rif valido. Por Ejemplo: V-12345678-8"),
		]
	)
	
	

			
	def __unicode__(self):
		ret = smart_unicode(self.nombre_est)
		while len(ret) < 20:
			ret = ret+" ."
		ret = ret+" ("+smart_unicode(self.propietario)+")"
		return ret

class Parametros(models.Model):
	estacionamiento = models.OneToOneField(Estacionamiento)
	capacidad = models.IntegerField(blank=False,null=False)
	hEntrada = models.TimeField(blank=True,null=True)
	hSalida = models.TimeField(blank=True,null=True)

	tarifa = models.DecimalField(max_digits=1000,decimal_places=2) 
	
	def __unicode__(self):
		return smart_unicode(self.estacionamiento.nombre_est)




	
class Reserva(models.Model):

	estacionamiento = models.ForeignKey(Estacionamiento)
	hEntrada = models.TimeField(blank=True,null=True)
	hSalida = models.TimeField(blank=True,null=True)

	def __unicode__(self):
		ret = smart_unicode(self.estacionamiento.nombre_est)
		while len(ret) < 20:
			ret = ret+" ."
		ret = ret+" "+smart_unicode(self.hEntrada.strftime("%H:%M"))+" - "
		ret = ret+smart_unicode(self.hSalida.strftime("%H:%M"))
		return ret