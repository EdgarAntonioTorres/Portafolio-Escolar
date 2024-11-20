# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

estudiantes = []

def agregar_estudiante(nombre, calificacion):
    estudiantes.append({"nombre": nombre,
                        "calificacion": calificacion})

def modificar_calificacion(nombre, nueva_calificacion):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            estudiante["calificacion"] = nueva_calificacion

def eliminar_estudiante(nombre):
    global estudiantes
    estudiantes = [e for e in estudiantes if e["nombre"] != nombre]

def mostrar_estudiantes():
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Calificación: {estudiante['calificacion']}")

def calcular_promedio():
    total_calificaciones = sum(e["calificacion"] for e in estudiantes)
    promedio = total_calificaciones / len(estudiantes)
    print(f"Calificaciones promedio = {promedio}")

#Ejemplo de Uso
agregar_estudiante("Richie", 10)
agregar_estudiante("Edgar", 10)
agregar_estudiante("Adrián", 8)
agregar_estudiante("Arangua", 7)
mostrar_estudiantes()
modificar_calificacion("Richie", 9)
mostrar_estudiantes()
calcular_promedio()
eliminar_estudiante("Adrián")
mostrar_estudiantes()