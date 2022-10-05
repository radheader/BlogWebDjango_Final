# Proyecto Python Final Webblog con Django

Este proyecto  fue llevado a cabo por **Cristian Camejo** ,  **Tomas Servin** y **Christian Rodriguez**. El lenguaje de programación es **Python** 3.9 bajo el framework **Django** 4.1.1

Este Blog con temática del mundial Qatar 2022 cuenta con Publicaciones, Registros de Estadios, Selecciones y Jugadores de parte de los usuarios, Perfiles de usuarios, Nosotros, Autenticación de Usuarios y finalmente la sección Admin de Django.


Presentación del Blog:
https://


Bajo la metodología agil del marco de trabajo en Scrum nos organizamos para que cada uno realizara tareas específicas, al localizarnos en latitudes diferentes, utilizamos Trello donde definimos los requirimientos y construimos las tarjetas como tareas a realizar en un tiempo determinado.

- Creación de proyecto base, layout y CSS(Cristian C.)
- Post, Inicio y Auhtentication (Cristian C.)
- Nosotros (Christian R.)
- Data (Tomas S.)
- Test (Christian R.)
- Publicacion video (Christian R.)

Instrucciones de instalación
===
1.- Clonar proyecto de Github por ssh o https
---

2.- Instalar entorno virtual
---
	python -m venv env
	source env/bin/activate 
  (Consola CMD ambiente_virtual\Scripts\activate.bat)

3- Ingresar a la carpeta app
---

4.- Instalar dependencias
---
	pip install -r requirements.txt
	pip freeze (Para verificar que se instalaron las dependencias)

5.- Ejecutar servidor web
---
	python manage.py runserver
  
6.- Acceder con user y password   vía
---
	127.0.0.1:8000/admin
  user **futbol01**
  password  **12345abcde**
