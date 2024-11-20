# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:31:23 2024

@author: Edgar 'Toño'
"""
import random

class AdivinaSuperheroe:
    def __init__(self):
        self.palabras = ["spiderman", "batman", "deadpool", "wolverine", "ironman", "flash", "superman", "daredevil", "invincible", "homelander", "wonder woman", "green lantern", "capitan america", "hulk", "cyborg", "robin", "spidergwen", "groot", "rocket", "gamora", "ant man", "thor", "black widow", "hawkeye", "doctor strange", "mr fantastic", "la mole", "drax", "starlord", "wasp", "moon knight", "falcon", "cyclops", "bestia", "storm", "profesor x", "black bolt", "blade", "ghost rider", "lobo"]
        # Selecciona una palabra al azar de la lista de palabras
        self.palabra_secreta = random.choice(self.palabras)
        self.intentos_maximos = 5
        self.intentos_restantes = self.intentos_maximos
        self.letras_adivinadas = ["_"] * len(self.palabra_secreta)

    def mostrar_estado(self):
        print("Palabra secreta:", " ".join(self.letras_adivinadas))
        print("Intentos restantes:", self.intentos_restantes)

    def adivinar_letra(self, letra):
        assert len(letra) == 1, "Por favor, introduce una sola letra."
        if letra in self.palabra_secreta:
            for i in range(len(self.palabra_secreta)):
                if self.palabra_secreta[i] == letra:
                    self.letras_adivinadas[i] = letra
            print("¡Bien hecho! Letra correcta.")
        else:
            self.intentos_restantes -= 1
            print("La letra no está en la palabra.")
        self.mostrar_estado()

    def adivinar_palabra(self, palabra):
        if palabra == self.palabra_secreta:
            self.letras_adivinadas = list(self.palabra_secreta)
            print("¡Felicidades! Has adivinado al superhéroe.")
        else:
            self.intentos_restantes -= 1
            print("No lograste adivinar, suerte para la próxima.")
        self.mostrar_estado()

    def jugar(self):
        print("Bienvenido al juego de adivinar al superheroe.")
        print("")
        while "_" in self.letras_adivinadas and self.intentos_restantes > 0:
            intento = input("Adivina una letra o la palabra completa: ").lower()
            print("")
            if len(intento) == 1:
                self.adivinar_letra(intento)
            elif len(intento) == len(self.palabra_secreta):
                self.adivinar_palabra(intento)
            else:
                print("Introduce una sola letra o la palabra completa del mismo tamaño que la palabra secreta.")
        if "_" not in self.letras_adivinadas:
            print("¡Ganaste el juego!")
        else:
            print("Se acabaron los intentos. La palabra era:", self.palabra_secreta)

# Código para ejecutar el juego
juego = AdivinaSuperheroe()
juego.jugar()
