# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:57:28 2024

@author: Edgar
"""

import time

class Auto:
    def __init__(self, nombre, velocidadMax, velocidadNormal, velocidadAdelantamiento):
        self.nombre = nombre
        self.velocidadMax = velocidadMax #km/h
        self.distanciaRecorrida = 0 #km
        self.velocidadNormal = velocidadNormal #km/h
        self.velocidadAdelantamiento = velocidadAdelantamiento #km/h
        
    def avanzar(self, tiempo):
        #Convertir la velocidad de km/h a km/s
        distancia = (self.velocidadNormal / 3600) * tiempo
        self.distanciaRecorrida += distancia
        
    def acelerar(self,tiempo):
        #Convertir la velocidad de km/h a km/s
        distancia = (self.velocidadMax / 3600) * tiempo
        self.distanciaRecorrida += distancia
        
    def adelantar(self,tiempo):
        #Convertir la velocidad de km/h a km/s
        distancia = (self.velocidadMax / 3600) * tiempo
        self.distanciaRecorrida += distancia
        
class Carrera:
    def __init__(self, longitudPista, autos):
        self.longitudPista = longitudPista #km
        self.autos = autos
        self.tiempoTotal = 0
        
    def simularCarrera(self, duracion):
        interval = 10 #Tiempo entre actualizaciones de posición
        tiempoTranscurrido = 0
        while tiempoTranscurrido < duracion:
            #Ordenar autos por la distancia recorrida para identificar los últimos
            autosOrdenados = sorted(self.autos, key=lambda auto: auto.distanciaRecorrida)
            ultimosAutos = autosOrdenados[:2]
            mediosAutos = autosOrdenados[3:6]
            
            for auto in self.autos:
                if auto in ultimosAutos:
                    auto.acelerar(interval)
                elif auto in mediosAutos:
                    auto.adelantar(interval)
                else:
                    auto.avanzar(interval)
            self.tiempoTotal += interval
            self.mostrarPosiciones()
            tiempoTranscurrido += interval
        
            #Verificar si lo autos han completado la carrera
            if all(auto.distanciaRecorrida >= self.longitudPista for auto in self.autos):
                break
            time.sleep(2.5)
    
    def mostrarPosiciones(self):
        print("Estado de la carrera:")
        autosOrdenados = sorted(self.autos, key=lambda auto: auto.distanciaRecorrida, reverse=True)
        for i, auto in enumerate(autosOrdenados, start=1):
            print(f"{i}. {auto.nombre}: {auto.distanciaRecorrida:.2f} km")
        print("")
        
    def mostrarResultados(self):
        print("Resultado de la carrera:")
        #Ordenar autos por distancia recorrida para determinar su posición final
        autosOrdenados = sorted(self.autos, key=lambda auto: auto.distanciaRecorrida, reverse=True)
        for i, auto in enumerate(autosOrdenados, start=1):
            print(f"{i}. {auto.nombre}: {auto.distanciaRecorrida:.2f} km")
        ganador = autosOrdenados[0]
        print("")
        print(f"El ganador es {ganador.nombre} con una distancia de {ganador.distanciaRecorrida:.2f} km")
        print(f"Tiempo total de la carrera: {self.tiempoTotal} segundos")
    
#Crear a los autos
auto1 = Auto("SSC Tuatara", 456, 356, 406)
auto2 = Auto("Koenigsegg Agera RS", 447, 347, 397)
auto3 = Auto("Hennessey Venom GT", 435, 335, 385)
auto4 = Auto("Bugatti Veyron Super Sport", 431, 331, 381)
auto5 = Auto("Rimac Nevera", 415, 315, 365)
auto6 = Auto("Aston Martin Valkyrie", 402, 302, 352)
auto7 = Auto("McLaren Speedtail", 403, 303, 353)
auto8 = Auto("Tesla Roadster", 402, 302, 352)

#Interfaz de inicio del juego
print("Bienvenido al simulador de carreras.")
print("")
distanciaPista = 0
duracionEscogida = 0

while (distanciaPista == 0):
    print("Elige una carrera:")
    seleccionCarrera = input("1. 24 horas de Le Mans \n2. Indianapolis 500 \n3. GP de Mónaco \n4. Daytona 500 \n5. Rally Dakar \n")
    if (seleccionCarrera == "1"):
        distanciaPista = 13626
    elif(seleccionCarrera == "2"):
        distanciaPista = 4023
    elif(seleccionCarrera == "3"):
        distanciaPista = 260
    elif(seleccionCarrera == "4"):
        distanciaPista = 805
    elif(seleccionCarrera == "5"):
        distanciaPista = 7891
    else:
        print("Error, intente de nuevo.")
print("")

while (duracionEscogida == 0):
    print("Selecciona la duración de la carrera:")
    seleccionCarrera = input("1. 10 segundos \n2. 30 segundos \n3. 1 minuto \n4. 1 minuto y medio \n5. 2 minutos \n")
    if (seleccionCarrera == "1"):
        duracionEscogida = 10
    elif(seleccionCarrera == "2"):
        duracionEscogida = 30
    elif(seleccionCarrera == "3"):
        duracionEscogida = 60
    elif(seleccionCarrera == "4"):
        duracionEscogida = 90
    elif(seleccionCarrera == "5"):
        duracionEscogida = 120
    else:
        print("Error, intente de nuevo.")
print("")

#Crear carrera
carrera = Carrera(distanciaPista, [auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8])
print("Inicio de la carrera: \n")
carrera.mostrarPosiciones()

#Simular carrera 60 segs
carrera.simularCarrera(duracionEscogida)

# Mostrar los resultados de la carrera
carrera.mostrarResultados()
