# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 05:29:18 2020

@author: PedroW10
"""

#Proyecto  grupal python 
#GRAFICOS ESTADISTICOS CON MATPLOTLIB
#TEMA: VIDEOJUEGOS
from faker import Faker
from faker.providers import internet
from faker_credit_score import CreditScore #usar para crear socre de juegos Fuente: https://faker.readthedocs.io/en/stable/providers.html
import pandas as pd
import random
fake = Faker()

####################################

# Numero de filas de la base a crear
numero_casos=100000

fecha = []
usuario = []
puntaje = []
juego = []
tipo_juego = []
tiempo_juego = []
posicion_jugador = []
nivel = []

for _ in range(numero_casos):
    #crea fechas de prueba
    fecha.append(fake.date(pattern='%Y-%m-%d', end_datetime=None))
    #crea usuarios de prueba
    usuario.append(fake.name())
    #crea puntaje de prueba
    puntaje.append(fake.credit_score_provider())
    #crea nombre de juego # reemplazar los nombres despues
    juego.append(fake.credit_score_provider())
    #crea usuarios de prueba
    tipo_juego.append(random.choice(["Aventura","Arcade","Estrategia", "Simulacion", "Rol", "Deportes", "Accion"]))
    #crea usuarios de prueba
    tiempo_juego.append(random.random())
    #crea usuarios de prueba
    posicion_jugador.append(random.choice(["Primero","Segundo","Tercero"]))
    #crea usuarios de prueba
    nivel.append(random.choice(["Facil","Intermedio","Dificil"]))


frame = { 'fecha': pd.Series(fecha), 'usuario': pd.Series(usuario), 'puntaje':pd.Series(puntaje), 'juego':pd.Series(juego), 'tipo_juego':pd.Series(tipo_juego), 'tiempo_juego':pd.Series(tiempo_juego), 'posicion_jugador':pd.Series(posicion_jugador), 'nivel':pd.Series(nivel)} 
df = pd.DataFrame(frame) #USAR ESTE DATAFRAME PARA LOS GRAFICOS