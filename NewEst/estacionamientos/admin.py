from django.contrib import admin
from estacionamientos.models import Estacionamiento,Parametros,Reserva
# Register your models here.

admin.site.register(Estacionamiento)
admin.site.register(Parametros)
admin.site.register(Reserva)
