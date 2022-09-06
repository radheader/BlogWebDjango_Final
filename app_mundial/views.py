
from typing import Dict

from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from app_mundial.models import  Estadios, Jugadores, Selecciones


# Create your views here.




def inicio(request):

      return render(request, "app_mundial/inicio.html")


def Estadios(request):
      
      return render(request, "app_mundial/Estadios.html") 


def Jugadores(request):

      
      return render(request, "app_mundial/Jugadores.html")


def Selecciones(request):

      return render(request, "app_mundial/Selecciones.html")




# Formulario a mano
# def curso_formulario(request):
#       if request.method == 'POST':
#             data_formulario: Dict = request.POST
#             curso = Curso(nombre=data_formulario['nombre'], comision=data_formulario['comision'])
#             curso.save()
#             return render(request, "AppCoder/inicio.html")
#       else:  # GET
#             return render(request, "AppCoder/form_curso.html")

# VISTAS DE jugadores





def Jugadores_formulario(request):
       if request.method == "POST":
             data_formulario: Dict = request.POST
             jugadores = Jugadores(['nombre'], edad=data_formulario['edad'], equipo=data_formulario['equipo'])
             jugadores.save()
             return render(request, "app_mundial/inicio.html")
       
       else:       #GET
           return render(request, "app_mundial/form_jugadores.html")