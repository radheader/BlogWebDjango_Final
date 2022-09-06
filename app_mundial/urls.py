from django.urls import path

from app_mundial import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('estadios/', views.Estadios, name="estadios"),
    path('selecciones/', views.Selecciones, name="selecciones"),

    path('jugadores/', views.Jugadores, name="jugadores"),
    path('crear-jugadores/', views.Jugadores_formulario, name="Jugadores_formulario"),
   
]
