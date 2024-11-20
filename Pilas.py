# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:16:39 2024

@author: Alumno
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(f"Agregando {dato} a la cima de la pila")
        # Si no hay datos, agregar el valor en el elemento superior
        if self.superior == None:
            self.superior = Nodo(dato)
        else:
            nuevo_nodo = Nodo(dato)
            nuevo_nodo.siguiente = self.superior
            self.superior = nuevo_nodo

    def desapilar(self):
        # Si no hay datos en el nodo superior, regresamos
        if self.superior == None:
            print("No hay ningún elemento")
            return 
        print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.siguiente

    def imprimir(self):
        print("Imprimiendo la pila")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"[{nodo_temporal.dato}]", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")

# Uso de la pila
pila = Pila()
pila.apilar("Leon S Kennedy")
pila.apilar("Bob Esponja")
pila.apilar("Henry Cavill")
pila.imprimir()
pila.desapilar()
pila.imprimir()