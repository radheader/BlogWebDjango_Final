from http.client import CONTINUE

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import  UpdateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from app_mundial.models import   Jugadores, Estadios, Selecciones
from app_mundial.forms import JugadoresFormulario, EstadiosFormulario, SeleccionesFormulario, UserRegisterForm, UserUpdateForm, AvatarFormulario

#Para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.




def inicio(request):

      return render(request, "app_mundial/inicio.html")

def about(request):

      return render(request, "app_mundial/about.html")


# Formulario Jugadores: Eliminar, Editar, Crear, Buscar
@login_required
def jugadores(request):
    jugadores = Jugadores.objects.all()
    contexto = {"jugadores": jugadores}
    borrado = request.GET.get('borrado',None)
    contexto['borrado'] = borrado

    return render(request, "app_mundial/jugadores.html", contexto)


def eliminar_jugadores(request, id):
    jugadores = Jugadores.objects.get(id=id)
    borrado_id = jugadores.id  
    jugadores.delete()
    url_final = f"{reverse('jugadores')}?borrado={borrado_id}"

    return redirect(url_final)


def editar_jugadores(request, id):
    jugadores = Jugadores.objects.get(id=id)
    if request.method == 'POST':
        formulario = JugadoresFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            jugadores.nombre = data['nombre']
            jugadores.edad = data['edad']
            jugadores.equipo = data['equipo']
            
            jugadores.save()

            return redirect(reverse('jugadores'))  

    else:  # GET
        inicial = {
            'nombre': jugadores.nombre,
            'edad': jugadores.edad,
            'equipo': jugadores.equipo,
            
        }
        formulario = JugadoresFormulario(initial=inicial)
    return render(request, "app_mundial/form_jugadores.html", {"formulario": formulario})
          


def crear_jugadores(request):
    if request.method == 'POST':
        formulario = JugadoresFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            jugadores = Jugadores(**data)
            jugadores.save()
            return redirect(reverse('jugadores'))
    else:  # GET
        formulario = JugadoresFormulario()  # Formulario vacio para construir el html
    return render(request, "app_mundial/form_jugadores.html", {"formulario": formulario})



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


# Formulario de Estadios: Eliminar, Editar, Crear, Buscar

@login_required
def estadios(request):
      estadios = Estadios.objects.all()
      contexto = {"estadios": estadios}
      borrado = request.GET.get("borrado", None)
      contexto ["borrado"]= borrado

      return render(request, "app_mundial/estadios.html", contexto)



def eliminar_estadios(id):
    estadios = Estadios.objects.get(id=id)
    borrado_id = estadios.id  
    estadios.delete()
    url_final = f"{reverse('estadios')}?borrado={borrado_id}"

    return redirect(url_final)


def editar_estadios(request, id):
    estadios = Estadios.objects.get(id=id)
    if request.method == 'POST':
        formulario = EstadiosFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            estadios.nombre = data['nombre']
            estadios.pais = data['pais']
            estadios.capacidad = data['capacidad']
            
            estadios.save()

            return redirect(reverse('estadios'))  

    else:  # GET
        inicial = {
            'nombre': estadios.nombre,
            'pais': estadios.pais,
            'capacidad': estadios.capacidad,
            
        }
        formulario = EstadiosFormulario(initial=inicial)
    return render(request, "app_mundial/form_estadios.html", {"formulario": formulario})
          



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



# Formulario de Selecciones: Eliminar, Editar, Crear, Buscar
@login_required
def selecciones(request):
      selecciones = Selecciones.objects.all()
      contexto = {"selecciones": selecciones}
      borrado = request.GET.get("borrado", None)
      return render(request, "app_mundial/selecciones.html", {"selecciones":selecciones})

def eliminar_selecciones(request, id):
    selecciones = Selecciones.objects.get(id=id)
    borrado_id = selecciones.id
    selecciones.delete()
    url_final = f"{reverse('selecciones')}?borrado={borrado_id}"

    return redirect(url_final)

def crear_selecciones(request):
    if request.method == 'POST':
        formulario = SeleccionesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            selecciones = Selecciones(**data)
            
            selecciones.save()
            return redirect(reverse('selecciones'))
    else:  # GET
        formulario = SeleccionesFormulario()  # Formulario vacio para construir el html
    return render(request, "app_mundial/form_seleccionesr.html", {"formulario": formulario})

def editar_selecciones(request, id):
    # Recibe param profesor id, con el que obtenemos el profesor
    selecciones = Selecciones.objects.get(id=id)

    if request.method == 'POST':
        formulario = SeleccionesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            selecciones.nombre = data['nombre']
            selecciones.confederacion = data['confederacion']
            selecciones.palmares = data['palmares']
            selecciones.save()

            return redirect(reverse('selecciones'))
    else:  # GET
        inicial = {
            'nombre': selecciones.nombre,
            'confedracion': selecciones.confederacion,
            'palmares': selecciones.palmares,
            
        }
        formulario = SeleccionesFormulario(initial=inicial)
    return render(request, "app_mundial/form_selecciones.html", {"formulario": formulario})      

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
       
# Views de usuario, registro, login o logout mas Avatar.
class ProfileUpdateView( UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'app_mundial/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


def agregar_avatar(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES) #aquí me llega toda la información del html

        if form.is_valid:   #Si pasó la validación de Django
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('inicio'))

    form = AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "app_mundial/form_avatar.html", {"form":form})


def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "app_mundial/inicio.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }
    
    return render(request, "app_mundial/registro.html", context = context )


def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            
            if user:
                login(request=request, user=user)
                if next_url:
                 return render(request, "app_mundial/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"app_mundial/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"app_mundial/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"app_mundial/login.html", {'form':form} )


class CustomLogoutView(LogoutView):
    template_name = "app_mundial/logout.html"  
    next_page = reverse_lazy("inicio") 
    
    



