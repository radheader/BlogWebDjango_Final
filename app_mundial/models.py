from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

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
     palmares = models.CharField(max_length=50)

     def __str__(self):
        return f'{self.nombre} - {self.confederacion} - {self.palmares}'

   


class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"
    
<<<<<<< HEAD
class blog(models.Model):
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + 'l' + str(self.author)
=======
class Tag (models.Model):
    name = models.CharField(max_length=200)

    def __Str__(self):
        return self.name


     
>>>>>>> 974f04552589113a2352e477a670c9e5dc9778ae
