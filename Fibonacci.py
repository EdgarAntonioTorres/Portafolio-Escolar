# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:43:30 2024

@author: edgar
"""

import time 

#Fibonacci sin recursividad
def fibonacci_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

#Ejemplo de uso 
numerito = 9
inicio = time.time()
print(f"La serie de fibonacci hasta {numerito} número es {fibonacci_1(numerito)}")
fin = time.time()
print(f"El tiempo de ejecucion es: {fin - inicio} s")

#Fibonacci con recursividad
def fibonacci_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
     return fibonacci_1(n-1) + fibonacci_1(n-2)
    
#Ejemplo de uso 
numerito = 9
inicio = time.time()
print(f"La serie de fibonacci hasta {numerito} número es {fibonacci_2(numerito)}")
fin = time.time()
print(f"El tiempo de ejecucion es: {fin - inicio} s")