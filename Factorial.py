# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:37:38 2024

@author: edgar
"""

import time 

#Factorial sin recursividad 
def factorial_1(n):
    tamal = 1
    for i in range(2, n+1):
        tamal = tamal * i
    return tamal 
#ejemplo de uso 
numerito = 5
inicio = time.time()
print(f"El factroial de {numerito} es {factorial_1(numerito)}")
fin = time.time()
print(f"El tiempo de ejecucion es: {fin - inicio} s")
    
    
#Factorial con recursividad 
def factorial_2(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial_2(n-1)
#ejemplo de uso 
inicio = time.time()
print(f"El factroial de {numerito} es {factorial_2(numerito)}")
fin = time.time()
print(f"El tiempo de ejecucion es: {fin - inicio} s")