# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:35:58 2024

@author: Alumno
"""

class HashTable:
    def __init__(self, size):
        #Método constructor para inicializar la tabla Hash
        self.size = size
        self.table = [[] for _ in range(size)] * size #Crear una lista del tamaño size
        
    def isEmpty(self):
        #Método para verificar si la tabla Hash está vacía
        for i in range(self.size):
            #Recorrer cada posición de la tabla
            if len(self.table[i]) > 0:
                #Si la lista en el índice i no está vacía la tabla no está vacía
                return False
            #Si todas las listas están vacías, la tabla está vacía
            return True
    
    def Size(self):
        #Método para obtener el número de elementos en una tabla hash
        grefg = 0
        for i in range(self.size):
            #Recorrermos cada posición de la tabla
            if self.table[i] is not None:
                #Si la posición no está vacía, aumentamos un contador
                grefg += len(self.table[i])
                #Sumar la cantidad de elementos en la lista del índice i
        return grefg #Devolver el número total de elementos
    
    def hashfunction(self, key):
        #Método para calcular el índice a partir de la clave
        if isinstance(key, int):
            #Si la clave es un entero, usamos el modulo del tamaño de la tabal
            return key % self.size
        elif isinstance(key, str):
            #Si la clave es una cadena, sumamos los valores que ASCII de sus caracteres
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
        
    def add(self, key, value):
        #Método para agregar una clave (llave) y su valor a la tabla hash
        index = self.hashfunction(key) #Calculamos el índice
        #Usando la función hash
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                #SI encontramos la clave, actualizar su valor
                self.table[index][i] = (key, value)
                #Actualizar el par clave, valor
                return
        #Si la clave no existe en la lista, agregamos el nuevo par clave, valor
        self.table[index].append((key,value))
        #agregar el par al final de la lista
    
    def getByKey(self, key):
        #Método para obtener un valor a partir de la clave
        index = self.hashfunction(key)
        #Recorrer la lista en el índice calculado
        for k, v in self.table[index]:
            if k == key:
                #Si encontramos la clave, devolvemos el valor asociado
                return v
        #SI no encontramos la clave, devolver None
        return None
    
    def getByValue(self, value):
        #Método para obtener una clave a partir de su valor
        for i in range(self.size):
            #Recorrer cada posición de la tabla
            for k, v in self.table[i]:
                #Recorremos cada par clave, valor en la lista del índice i
                if v == value:
                    #Si encontramos el valor, devolver la clave asociada
                    return k
            #Sino encontramos el valor, devolver None
            return None
        #Sino encontramos el valor, devolvemos None
        return None
    
#Creamos una tabla hash de tamaño definido
hash_table = HashTable(5)

#Agregamos dos claves que generan el mismo índice
hash_table.add(1, "valor1") #hashfunction(1) % 5 --> 1
hash_table.add(6, "valor2") #hashfunction(6) % 5 --> 1

#Obtenemos los valores de ambas claves
print(hash_table.getByKey(1)) # --> Devolver "valor1"
print(hash_table.getByKey(6)) # --> Devolver "valor2"