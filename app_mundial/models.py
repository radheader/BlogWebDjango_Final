from django.db import models

# Create your models here.


class Estadios(models.Model):
    nombre = models.CharField(max_length=500)
    pais = models.CharField(max_length=500)
    capacidad = models.IntegerField()
    

 


class Jugadores(models.Model):
    nombre = models.CharField(max_length=128)
    edad = models.IntegerField()
    
    


class Selecciones(models.Model):
     nombre = models.CharField(max_length=128)
     confederacion = models.CharField(max_length=128)
     palmares = models.CharField(max_length=128)

   



    
