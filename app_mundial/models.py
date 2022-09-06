from django.db import models

# Create your models here.


class Estadios(models.Model):
    nombre = models.CharField(max_length=500)
    pais = models.CharField(max_length=500)
    capacidad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.pais} - {self.capacidad}'
    

 


class Jugadores(models.Model):
    nombre = models.CharField(max_length=128)
    edad = models.IntegerField()
    equipo = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.nombre} - {self.edad} - {self.equipo}'
    


class Selecciones(models.Model):
     nombre = models.CharField(max_length=128)
     confederacion = models.CharField(max_length=128)
     palmares = models.CharField(max_length=128)

     def __str__(self):
        return f'{self.nombre} - {self.confederacion} - {self.palmares}'

   



    
