# Entregable2Camejo
## En este proyecto creamos una Web del Mundial, donde se pueden crear Estadios, Selecciones y Jugadores.
  Como el Munial no comenzo todavia, se pueden agregar y borrar diferentes Selecciones y Jugadores si tienes acceso al admin de la Web.

## Entregable2-entrega_coder-app_mundial

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona el proyecto
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user(futbol01) y password(12345abcde) via:
```
127.0.0.1:8000/admin
```
## Instrucciones para poder entrar en la Web-Mundial y poder ver y crear Estadios, Jugadores y Selecciones.
+ Hacer las Instrucciones de instalado en  Proyecto local
+ ir a la Terminal
+ Ubicarse en la carpeta madre
+ Abrir la Web con python manage.py runserver
+ 127.0.0.1:8000, aparecera una pagina de page not found (404)
+ En el servidor escribimos estos para poder ver la Web: http://127.0.0.1:8000/mundial-site/
+ Nos aparecera la Web
+ Podemos entrar en las diferentes pestañas: Estadios, Selecciones, Jugadores.
+ En cada una de ellas, podremos agregar y buscar ej: en la pestaña Jugadores, podremos agregar Jugadores, en su respectivo (Agregar Jugadores), y buscar Jugadores en su respectivo (Busar Jugadores).

## Tecnologia Utilizada
+ Python/Django
+ Html
+ Css
+ sqlite

## Personas Desarolladoras del Proyecto
+ Cristian Camejo
+ Christian Rodriguez Torres
+ Tomas Servin
