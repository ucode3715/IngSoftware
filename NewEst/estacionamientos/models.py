
from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import RegexValidator
#from django import forms

# Create your models here.

class Estacionamiento(models.Model):
	propietario = models.CharField(max_length=64,null = False, blank = False, 
		validators=[RegexValidator
			(regex='^( |[a-zA-Z])*$',
			message="Debe ser un nombre de persona"),
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
		return smart_unicode(self.nombre_est)

class Parametros(models.Model):
	estacionamiento = models.ForeignKey(Estacionamiento)
	capacidad = models.IntegerField(blank=False,null=False)
	hEntrada = models.CharField(max_length=64,
		validators=[RegexValidator
			    (regex='(1[0-2]|[1-9]):[0-5][0-9](\\s)(a|p)m$',
			     message="Debe una hora valida. Por Ejemplo: 9:00 am "),
			    ])
	hSalida = models.CharField(max_length=64,
				   validators=[RegexValidator
					       (regex='(1[0-2]|[1-9]):[0-5][0-9](\\s)(a|p)m$',
						message="Debe una hora valida. Por Ejemplo: 9:00 pm "),
		])
	tarifa = models.DecimalField(max_digits=1000,decimal_places=2) 
	
	def __unicode__(self):
		return smart_unicode(self.estacionamiento.nombre_est)
