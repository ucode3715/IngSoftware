from django import forms

from models import Estacionamiento,Parametros

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento

class ParametrosForm(forms.ModelForm):
    class Meta:
        model = Parametros
    
