from typing import Dict

from django.shortcuts import render, redirect, reverse

from app_mundial.models import   Jugadores, Estadios, Selecciones
from app_mundial.forms import JugadoresFormulario, EstadiosFormulario, SeleccionesFormulario






# Create your views here.




def inicio(request):

      return render(request, "app_mundial/inicio.html")


def estadios(request):
      estadios = Estadios.objects.all()
      return render(request, "app_mundial/estadios.html", {"estadios": estadios}) 


def jugadores(request):
      jugadores = Jugadores.objects.all()
      return render(request, "app_mundial/jugadores.html", {"jugadores": jugadores})
      
      


def selecciones(request):
      selecciones = Selecciones.objects.all()
      return render(request, "app_mundial/selecciones.html", {"selecciones":selecciones})






# VISTAS DE jugadores
# Formulario echo a mano
#def jugadores_formulario(request):
#       if request.method == "POST":
#            data_formulario: Dict = request.POST
#             jugadores = Jugadores(nombre=data_formulario['nombre'], edad=data_formulario['edad'], equipo=data_formulario['equipo'])
#             jugadores.save()
#             return render(request, "app_mundial/inicio.html")
#       
#       else:       #GET
#             return render(request, "app_mundial/form_jugadores.html")


# Formulario Selecciones
# Formulario con (api form django)
def jugadores_formulario(request):
       if request.method == "POST":
            formulario = JugadoresFormulario (request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  jugadores = Jugadores(nombre=data['nombre'], edad=data['edad'], equipo=data['equipo'])
                  jugadores.save()
                  return render(request, "app_mundial/inicio.html", {"exitoso": True})

       else:
            formulario = JugadoresFormulario() # Formulario vacio para construir el HTML
       return render( request, "app_mundial/form_jugadores.html",{"formulario": formulario})      

def busqueda_jugadores(request):
      return render( request, "app_mundial/form_busqueda_jugadores.html")


            
def buscar_jugadores(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        jugadores = Jugadores.objects.filter(nombre__icontains=nombre)
        return render(request, "app_mundial/jugadores.html", {'jugadores': jugadores})
    else:
        return render(request, "app_mundia/jugadores.html", {'jugadores': []}) 

# Formulario de Estadios

def estadios_formulario(request):
       if request.method == "POST":
            formulario = EstadiosFormulario (request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  estadios = Estadios(nombre=data['nombre'], pais=data['pais'], capacidad=data['capacidad'])
                  estadios.save()
                  return render(request, "app_mundial/inicio.html", {"exitoso": True})

       else:
            formulario = EstadiosFormulario()
       return render( request, "app_mundial/form_estadios.html",{"formulario": formulario})      

def busqueda_estadios(request):
      return render( request, "app_mundial/form_busqueda_estadios.html")


            
def buscar_estadios(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estadios = Estadios.objects.filter(nombre__icontains=nombre)
        return render(request, "app_mundial/estadios.html", {'estadios': estadios})
    else:
        return render(request, "app_mundia/estadios.html", {'estadios': []})      



# Formulario de Selecciones

def selecciones_formulario(request):
       if request.method == "POST":
            formulario = SeleccionesFormulario (request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  selecciones = Selecciones(nombre=data['nombre'], confederacion=data['confederacion'], palmares=data['palmares'])
                  selecciones.save()
                  return render(request, "app_mundial/inicio.html", {"exitoso": True})

       else:
            formulario = SeleccionesFormulario()
       return render( request, "app_mundial/form_selecciones.html",{"formulario": formulario})      

def busqueda_selecciones(request):
      return render( request, "app_mundial/form_busqueda_selecciones.html")


            
def buscar_selecciones(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        selecciones = Selecciones.objects.filter(nombre__icontains=nombre)
        return render(request, "app_mundial/selecciones.html", {'selecciones': selecciones})
    else:
        return render(request, "app_mundia/selecciones.html", {'selecciones': []})             
       