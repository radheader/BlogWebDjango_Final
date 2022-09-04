from django.urls import path

from app_mundial import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('estadios/', views.Estadios, name="estadios"),
    path('jugadores/', views.Jugadores, name="jugadores"),
    path('selecciones/', views.Selecciones, name="selecciones"),
   
]
