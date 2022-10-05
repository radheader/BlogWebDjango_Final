# Create your tests here.

import random
import string
from django.forms import IntegerField

from django.test import TestCase
from app_mundial.views import jugadores
from app_mundial.models import Jugadores 
from app_mundial.models import Estadios
from django.contrib.auth.models import User

class JugadoresTestCase(TestCase):

    def test_creacion_jugadores(self):

        # Test 1: Comprobar puedo crear un jugador con un nombre con letras random y edad random
        lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_equipo = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        nombre_prueba = "".join(lista_letras_nombre)
        equipo_prueba = "".join(lista_letras_equipo)
        edad_prueba = random.choice(range(1,121))     
        jugador_1 = Jugadores.objects.create(nombre=nombre_prueba, equipo=equipo_prueba, edad=edad_prueba)

        self.assertIsNotNone(jugador_1.id)
        self.assertEqual(jugador_1.nombre, nombre_prueba)
        self.assertEqual(jugador_1.equipo, equipo_prueba)
        self.assertEqual(jugador_1.edad, edad_prueba)

    def test_editar_jugador(self):

        # Test 2: Comprobar que la edición de los datos de un jugador sea correcta 
        jugador_2 = Jugadores.objects.create(nombre="Armando Maradona", equipo="Boca Juniors", edad=24)
        jugador2_id = jugador_2.id
        nuevo_jugador = Jugadores.objects.get(id=jugador2_id)
        nombre_prueba = "Teofilo Cubillas"
        equipo_prueba = "Alianza Lima"
        edad_prueba = 28

        nuevo_jugador.nombre = nombre_prueba
        nuevo_jugador.edad = edad_prueba
        nuevo_jugador.equipo = equipo_prueba
        nuevo_jugador.save()
        nuevo_jugador_prueba = Jugadores.objects.get(id=nuevo_jugador.id)

        self.assertIsNotNone(nuevo_jugador_prueba.id)
        self.assertEqual(nuevo_jugador_prueba.nombre, nombre_prueba)
        self.assertEqual(nuevo_jugador_prueba.equipo, equipo_prueba)
        self.assertEqual(nuevo_jugador_prueba.edad, edad_prueba)

    def test_editar_estadio(self):

        # Test 3: Comprobar que la edición de los estadios sea correcta 
        estadio_2 = Estadios.objects.create(nombre="Alberto Gallardo", pais = "Peru", capacidad = 30000)
        estadio2_id = estadio_2.id
        nuevo_estadio = Estadios.objects.get(id=estadio2_id)
        nombre_prueba = "Estadio Nacional"
        pais_prueba = "Peru"
        capacidad_prueba = 45000

        nuevo_estadio.nombre = nombre_prueba
        nuevo_estadio.pais = pais_prueba
        nuevo_estadio.capacidad = capacidad_prueba
        nuevo_estadio.save()
        nuevo_estadio_prueba = Estadios.objects.get(id=nuevo_estadio.id)

        self.assertIsNotNone(nuevo_estadio_prueba.id)
        self.assertEqual(nuevo_estadio_prueba.nombre, nombre_prueba)
        self.assertEqual(nuevo_estadio_prueba.pais, pais_prueba)
        self.assertEqual(nuevo_estadio_prueba.capacidad, capacidad_prueba)