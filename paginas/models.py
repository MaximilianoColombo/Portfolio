from django.db import models

class Estudios(models.Model):
    institucion=models.CharField(max_length=200)
    periodo=models.CharField(max_length=15)
    titulo=models.CharField(max_length=100)
    estado=models.CharField(max_length=50)

class ExperienciaLaboral(models.Model):
    lugar=models.CharField(max_length=100)
    puesto=models.CharField(max_length=50)
    descripcion=models.TextField()
    periodo=models.CharField(max_length=15)
    icono=models.TextField()

class Servicios(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    icono=models.TextField()

class Proyecto (models.Model):
    titulo= models.CharField(max_length=250)
    tecnologia=models.CharField(max_length=50)
    link=models.CharField(max_length=200)
    imagen=models.TextField()

class datosPersonales(models.Model):
    nombreCompleto=models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=150)
    correo=models.CharField(max_length=150)
    celular=models.CharField(max_length=20)
    edad=models.IntegerField()
    fechaNacimiento=models.DateField()
    biografia=models.TextField()
    linkedin=models.CharField(max_length=100)
    github=models.CharField(max_length=100)

class Habilidades(models.Model):
    nombre=models.CharField(max_length=100)
    link=models.TextField()
    imagen=models.CharField(max_length=50)