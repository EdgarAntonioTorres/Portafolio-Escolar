# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:35:58 2024

@author: Alumno
"""

class HashTable:
    def __init__(self, size):
        #Método constructor para inicializar la tabla Hash
        self.size = size
        self.table = [None] * size #Crear una lista del tamaño size
        
    def isEmpty(self):
        #Método para verificar si la tabla Hash está vacía
        for i in range(self.size):
            #Recorrer cada posición de la tabla
            if self.table[i] is not None:
                return False
        #Si encontramos una posición no vacía, la tabla no está vacía
    
    def Size(self):
        #Método para obtener el número de elementos en una tabla hash
        grefg = 0
        for i in range(self.size):
            #Recorrermos cada posición de la tabla
            if self.table[i] is not None:
                #Si la posición no está vacía, aumentamos un contador
                grefg += 1
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
        self.table[index] = key, value
        #Almacenamos el par key-value en el index calculado
    
    def getByKey(self, key):
        #Método para obtener un valor a partir de la clave
        index = self.hashfunction(key)
        if self.table[index] is not None:
            #Si en ese índice hay un elemento
            if self.table[index][0] == key:
                #Y la clave coincide devolvemos el valor asociado
                return self.table[index][1]
        #Sino encontramos la clave, devolvemos None
        return None
    
    def getByValue(self, value):
        #Método para obtener una clave a partir de su valor
        for i in range(self.size):
            #Recorrer cada posición de la tabla
            if self.table[i] is not None:
                #Si la posición no está vacía
                if self.table[i][1] == value:
                    #Y el valor coincide, devolvemos la clave asociada
                    return self.table[i][0]
        #Sino encontramos el valor, devolvemos None
        return None
    
    
    
    
#Creamos una tabla hash de tamaño definido
hash_table = HashTable(5)

#Agregamos dos claves que generan el mismo índice
#hash_table.add(1, "valor1") #hashfunction(1) % 5 --> 1
hash_table.add(6, "valor2") #hashfunction(6) % 5 --> 1

#Obtenemos los valores de ambas claves
#print(hash_table.getByKey(1)) # --> Devolver "valor1"
print(hash_table.getByKey(6)) # --> Devolver "valor2"
                