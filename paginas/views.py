from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
  template = loader.get_template('index.html')
  servicios = Servicios.objects.all().values()
  persona= datosPersonales.objects.first()
  context = {
    'servicios': servicios,
    'persona':persona
  }
  return HttpResponse(template.render(context, request))

def about(request):
  template = loader.get_template('about.html')
  estudios = Estudios.objects.all().values()
  expLaboral= ExperienciaLaboral.objects.all().values()
  persona= datosPersonales.objects.first()
  habilidades= Habilidades.objects.all().values()
  context = {
    'estudios': estudios,
    'persona':persona,
    'experiencia': expLaboral,
    'habilidades':habilidades
  }
  return HttpResponse(template.render(context, request))

def projects(request):
  template = loader.get_template('projects.html')
  proyectos= Proyecto.objects.all().values()
  context = {
    'proyectos':proyectos
  }
  return HttpResponse(template.render(context, request))