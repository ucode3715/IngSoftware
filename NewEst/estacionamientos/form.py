from django import forms

from models import Estacionamiento,Parametros,Reserva,Pago

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento

class ParametrosForm(forms.ModelForm):
    class Meta:
        model = Parametros

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva 
        

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago