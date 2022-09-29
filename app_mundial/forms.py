

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_mundial.models import Avatar


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


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', ]


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']        


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']

