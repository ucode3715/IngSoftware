from django.shortcuts import render_to_response,render,RequestContext
from django.template import RequestContext


# Create your views here.
from estacionamientos.models import Estacionamiento
from django.http import HttpResponseRedirect
from form  import EstacionamientoForm,ParametrosForm


def lista_estacionamientos(request):
    estacionamiento = Estacionamiento.objects.all()
    return render_to_response('lista_estacionamientos.html',{'lista':estacionamiento}, context_instance=RequestContext(request))


def agregar(request):
    form = EstacionamientoForm(request.POST)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("agregar.html",locals(),context_instance = RequestContext(request))

def parametrizar(request):
    form = ParametrosForm(request.POST)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("parametrizar.html",locals(),context_instance = RequestContext(request))

def done(request):
    estacionamiento = Estacionamiento.objects.all()
    return render_to_response('done.html',{'lista':estacionamiento}, context_instance=RequestContext(request))

           
   
