# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:06:39 2024

@author: Edgar Torres
"""

def Busqueda_Binaria(lista, elemento):
    #Si la lisa está vacía retornar -1
    if not lista:
        return -1
    #Calcilar el punto medio de la lista
    medio = len(lista)//2 #int(lin(lista) / 2)
     
    #Verificar si el elemento está en el medio
    if lista[medio] == elemento:
        return medio
     
    #Si el elemento es mayor, buscar en la mitad derecha
    elif lista[medio] < elemento:
        lista_derecha = lista[medio + 1 :]
        #Buscar el elemento en la sublista derecha
        subresultado = Busqueda_Binaria(lista_derecha, elemento)
        
        #Si el elemento se encuentra en la sublista derecha ajustar el indice
        if subresultado != -1:
            return medio + 1 + subresultado
            #Ajustar indice con la posicion del subarreglo
        else:
            return -1            
        
    #Si el elemento es menor, buscar en la mitad izquierda
    else:
        return Busqueda_Binaria(lista[: medio], elemento)
    
#Ejemplo de uso
#Recordar que la lista debe de estar ordenada
lista = [2,3,5,7,11,13,17,19,23,29,31]
print(lista)
elemento_a_buscar = int(input("Inserte el número a buscar: "))
resultado = Busqueda_Binaria(lista, elemento_a_buscar)

if resultado != -1:
    print(f"El número {elemento_a_buscar} está en el índice {resultado}")
else:    
    print("El elemento a buscar no está en la lista")