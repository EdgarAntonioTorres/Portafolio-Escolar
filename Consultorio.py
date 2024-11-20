# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:44:35 2024

@author: Alumno
"""

class Paciente:
    def __init__(self, nombre, hora):
        self.nombre = nombre
        self.hora = hora
    def __str__(self):
        return f"{self.nombre}, hora de llegada: {self.hora}"
        
class Cola:
    def __init__(self):
        #Crea la cola
        self.pacientes = []
    def is_empty(self):
        #Verificar que la cola esta vacia
        return len(self.pacientes) == 0
    def encolar(self, nombre, hora):
        #Agregar un elemento al rear de la cola
        paciente = Paciente(nombre, hora)
        self.pacientes.append(paciente)
        print(f"El paciente {nombre}, ha sido añadido a las {hora}\n")
    def desencolar(self):
        #Eliminamos el elemento frontal
        if self.is_empty():
            raise IndexError("La cola está vacía")
        else: 
            print(f"El paciente {self.pacientes[0]} ha sido atendido")
        return  self.pacientes.pop(0)
    def size(self):
        #Obtener el tamaño de la cola
        return len(self.pacientes)
    def peek(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        print(f"El siguiente paciente es: {self.pacientes[0]}\n")
    
def menu():
    print("--------------------------------")
    print("Escoja una de las opciones:")
    print("\t1. Añadir paciente")
    print("\t2. Ver al siguiente paciente")
    print("\t3. Atender al paciente")
    print("\t4. Salir")
    print("--------------------------------")
    
def main():
    queue = Cola()
    opcion = 0
    
    while opcion != 4:
        menu()
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            nombre = input("Introduzca el nombre del paciente: ")
            hora = input("Introduzca la hora de llegada: ")
            print()
            queue.encolar(nombre, hora)
        elif opcion == 2:
            if not queue.is_empty():
                queue.peek()
            else:
                print("La cola está vacía\n")
        elif opcion == 3:
            if not queue.is_empty():
                queue.desencolar()
            else:
                print("La cola está vacía\n")
        elif opcion == 4:
            print("Saliendo del programa...")
        else:
            print("Opción no válida, intente de nuevo. \n")
            
main()