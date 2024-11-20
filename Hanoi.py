# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:13:09 2024

@author: Edgar Torres
"""

def Hanoi(a,b,c,n):
    #Nota 
    #a es origen
    #b es destino
    #c es auxiliar
    #Caso base: Si solo hay un disco, se mueve directamente del origen al destino
    if n == 1:
        print(f"Moverl disco 1 de la torre {a} a la torre {b}")
        return None

    #Mover los n-1 discos de origen a auxiliar usando destino como apoyo
    Hanoi(a,c,b,n-1)
    
    #Mover el disco n de origen a destino
    print(f"Mover disco {n} de la torre {a} a la torre {b}")
    
    #Mover n-1 discos de auxiliar a destino usando origen como apoyo
    Hanoi(c,b,a,n-1)
    
#Ejemplo de uso
n = 3
Hanoi("A", "B", "C", n)