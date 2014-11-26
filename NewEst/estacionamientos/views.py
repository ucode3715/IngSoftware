# coding= utf-8
from django.shortcuts import render_to_response,render,RequestContext
from django.template import RequestContext
import re

# Create your views here.
from estacionamientos.models import Estacionamiento,Reserva,Parametros
from django.http import HttpResponseRedirect
from django.utils.encoding import smart_unicode
from form  import EstacionamientoForm,ParametrosForm,ReservaForm

import re
def lista_estacionamientos(request):
    estacionamiento = Estacionamiento.objects.all()
    return render_to_response('lista_estacionamientos.html',{'lista':estacionamiento}, context_instance=RequestContext(request))


def agregar(request):
	form = EstacionamientoForm(request.POST)
	if form.is_valid():
		#Hay inconvenientes para la verificación de caracteres con acentos y eñes
		#reNombre = re.compile('^([ ñÑáéíóúÁÉÍÓÚa-zA-Z])*$')
		#if (reNombre.match(form.cleaned_data['propietario']) == None):
		#	errort = "El propietario debe tener un nombre de persona"
		#else:
		success = "Agregado satisfactoriamente"
		form.save(commit=True)
	return render_to_response("agregar.html",locals(),context_instance = RequestContext(request))

def parametrizar(request):
    form = ParametrosForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['hSalida'] < form.cleaned_data['hEntrada']:
            errort = 'La hora de salida debe ser mayor a la hora de entrada'
        else:
            form.save(commit=True)
    return render_to_response("parametrizar.html",locals(),context_instance = RequestContext(request))

def done(request):
    estacionamiento = Estacionamiento.objects.all()
    return render_to_response('done.html',{'lista':estacionamiento}, context_instance=RequestContext(request))

def reserva(request):
    form = ReservaForm(request.POST)
    if form.is_valid():
		horaEntrada = form.cleaned_data["hEntrada"]
		horaSalida = form.cleaned_data["hSalida"]
		# Verificacion de reserva mayor a 1h
		if ( horaSalida.hour - horaEntrada.hour) < 1:
			errort = "Debes reservar por al menos 1 hora"
			return render_to_response("reserva.html",locals(),context_instance = RequestContext(request))
		
		est=form.cleaned_data["estacionamiento"]
		par=Parametros.objects.get(estacionamiento=est)
		# Verificar reserva dentro del horario del estacionamiento
		if (horaEntrada < par.hEntrada) or (horaSalida > par.hSalida):
			errort = "Estacionamiento cerrado en ese horario"
			return render_to_response("reserva.html",locals(),context_instance = RequestContext(request))
			
		# Filtrar reservas por hora y estacionamiento
		reserva = Reserva.objects.filter(estacionamiento = est)
		# Reserva existente se encuentra dentro del intervalo solicitado
		reserva1 = reserva.filter( hEntrada__gte = horaEntrada,hSalida__lte = horaSalida)
		# Reserva existente abarca por completo el intervalo solicitado
		reserva2 = reserva.filter( hEntrada__lt = horaEntrada,hSalida__gt = horaSalida)
		# Reserva existente empieza antes del intervalo solicitado y termina dentro del intervalo solicitado
		reserva3 = reserva.filter( hEntrada__lt = horaEntrada, hSalida__gt = horaEntrada,hSalida__lt = horaSalida)
		# Reserva existente empieza dentro del intervalo solicitado y termina despues del intervalo solicitado
		reserva4 = reserva.filter( hEntrada__gt = horaEntrada, hEntrada__lt = horaSalida, hSalida__gt = horaSalida)
			
		numReservas = reserva1.count() + reserva2.count() + reserva3.count() + reserva4.count()
		# Verificar espacio disponible dentro del estacionamiento		
		if numReservas >= par.capacidad : 
			errort="No hay disponibilidad" 
		else:
			save_it = form.save()
			errort="Reserva realizada satisfactoriamente" 
    return render_to_response("reserva.html",locals(),context_instance = RequestContext(request))

def detalle(request):
    estacionamiento = Estacionamiento.objects.get(nombre_est=request.GET.get('nombre_est'))
    parametros = Parametros.objects.get(estacionamiento=estacionamiento)
    return render_to_response('detalle.html',{'est':estacionamiento, 'par':parametros}, context_instance=RequestContext(request))
