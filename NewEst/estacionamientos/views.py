from django.shortcuts import render_to_response,render,RequestContext
from django.template import RequestContext


# Create your views here.
from estacionamientos.models import Estacionamiento,Reserva,Parametros
from django.http import HttpResponseRedirect
from form  import EstacionamientoForm,ParametrosForm,ReservaForm


def lista_estacionamientos(request):
    estacionamiento = Estacionamiento.objects.all()
    return render_to_response('lista_estacionamientos.html',{'lista':estacionamiento}, context_instance=RequestContext(request))


def agregar(request):
    form = EstacionamientoForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return render_to_response("agregar.html",locals(),context_instance = RequestContext(request))

def parametrizar(request):
    form = ParametrosForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['hSalida'] > form.cleaned_data['hEntrada']:
            raise forms.ValidationError('Hora de salida debe ser mayor a hora de entrada')
        else:
            form.save(commit=True)
    return render_to_response("parametrizar.html",locals(),context_instance = RequestContext(request))

def done(request):
    estacionamiento = Estacionamiento.objects.all()
    return render_to_response('done.html',{'lista':estacionamiento}, context_instance=RequestContext(request))

def reserva(request):
    form = ReservaForm(request.POST)
    if form.is_valid():
        reservas = Reserva.objects.filter(
            hEntrada__gte =  form.cleaned_data["hEntrada"]
            ).filter(
            hSalida__gte = form.cleaned_data["hSalida"]
            )  
        est=form.cleaned_data["estacionamiento"]
        par=Parametros.objects.get(estacionamiento=est)
        if reservas.count() == par.capacidad : 
            errort="No hay disponibilidad" 
        else:
            save_it = form.save()
    return render_to_response("reserva.html",locals(),context_instance = RequestContext(request))

def detalle(request):
    estacionamiento = Estacionamiento.objects.get(nombre_est=request.GET.get('nombre_est'))
    parametros = Parametros.objects.get(estacionamiento=estacionamiento)
    return render_to_response('detalle.html',{'est':estacionamiento, 'par':parametros}, context_instance=RequestContext(request))
