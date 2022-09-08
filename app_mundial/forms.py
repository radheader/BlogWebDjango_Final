from django import forms



class JugadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    equipo = forms.CharField(max_length=50)

class EstadiosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    pais = forms.CharField(max_length=50)
    capacidad = forms.IntegerField()   


class SeleccionesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    confederacion = forms.CharField(max_length=50)
    palmares = forms.CharField(max_length=50)         