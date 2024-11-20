# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:22:31 2024

@author: Edgar 'Toño'
"""

class Pokemon:
    def __init__(self, nombre, tipo, hp, ataque, defensa, ataespecial, defespecial):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.ataespecial = ataespecial
        self.defespecial = defespecial
        
    def atacar(self, oponente):
        # Simplemente aplicamos el ataque del Pokémon al HP del oponente
        oponente.recibir_danio(self.ataque)

    def recibir_danio(self, danio):
        # Reduce HP según el daño recibido
        self.hp -= (danio - self.defensa)
        
    def atacar_especial(self, oponente):
        # Simplemente aplicamos el ataque del Pokémon al HP del oponente
        oponente.recibir_danio_especial(self.ataespecial)
        
    def recibir_danio_especial(self, danio):
        # Reduce HP según el daño recibido
        self.hp -= (danio - self.defespecial)

    def esta_vivo(self):
        # Verifica si el Pokémon todavía tiene HP positivo
        return self.hp > 0
    
    def curar(self):
        self.hp += 10
    
class BatallaPokemon:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turno = 1

    def aplicar_debilidad(self, atacante, defensor):
        debilidades = {'Agua': 'Fuego', 'Planta': 'Agua', 'Fuego': 'Planta'}
        if defensor.tipo == debilidades.get(atacante.tipo):
            defensor.defensa -= 1
            defensor.defespecial -= 4
            print(f"{defensor.nombre} tiene debilidad contra tipo {atacante.tipo}. Defensa reducida a {defensor.defensa}, Defensa especial reducida a {defensor.defespecial}.")
            
    def mostrar_estado(self):
        # Imprime el estado actual de cada Pokémon
        print(f"-----Turno: {self.turno}-----")
        print(f"{self.pokemon1.nombre} HP: {self.pokemon1.hp}")
        print(f"{self.pokemon2.nombre} HP: {self.pokemon2.hp}")
        print("")

    def ejecutar_turno(self, accion_pokemon1, accion_pokemon2):
        # Procesa los ataques según las acciones
        if accion_pokemon1 == "A":
            self.pokemon1.atacar(self.pokemon2)
        if accion_pokemon2 == "A":
            self.pokemon2.atacar(self.pokemon1)
        if accion_pokemon1 == "AE":
            self.pokemon1.atacar_especial(self.pokemon2)
        if accion_pokemon2 == "AE":
            self.pokemon2.atacar_especial(self.pokemon1)
        if accion_pokemon1 == "C":
            self.pokemon1.curar()
        if accion_pokemon2 == "C":
            self.pokemon2.curar()
            
        # Incrementa el contador de turnos
        self.turno += 1
        
# Crear los Pokémon
class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fuego", 60, 16, 6, 24, 9)
class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Agua", 60, 12, 8, 18, 12)
class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Planta", 60, 12, 6, 24, 12)

# Elegir los Pokémon
def seleccionar_pokemon():
    while True:
        eleccion = input("Elige un Pokémon (Charmander, Squirtle, Bulbasaur): ").lower()
        if eleccion == "charmander":
            return Charmander()
        elif eleccion == "squirtle":
            return Squirtle()
        elif eleccion == "bulbasaur":
            return Bulbasaur()
        print("Pokémon desconocido, intenta de nuevo.")

# Crear la batalla
print("¡Bienvenido al simulador de batallas Pokémon!")
print("---------------------------------------------")
pokemon1 = seleccionar_pokemon()
pokemon2 = seleccionar_pokemon()
print("")
batalla = BatallaPokemon(pokemon1, pokemon2)

# Ejecutar la batalla
batalla.aplicar_debilidad(pokemon1,pokemon2)
batalla.aplicar_debilidad(pokemon2,pokemon1)
while pokemon1.esta_vivo() and pokemon2.esta_vivo():
    batalla.mostrar_estado()
    accion_pokemon1 = input(f"Turno de {pokemon1.nombre} - Elige un movimiento:\n A: Atacar\n AE: Ataque especial\n C: Curar\n").upper()
    accion_pokemon2 = input(f"Turno de {pokemon2.nombre} - Elige un movimiento:\n A: Atacar\n AE: Ataque especial\n C: Curar\n").upper()
    print("")
    batalla.ejecutar_turno(accion_pokemon1, accion_pokemon2)

# Mostrar el resultado de la batalla
if pokemon1.esta_vivo():
    print(f"¡{pokemon1.nombre} ha ganado la batalla!")
else:
    print(f"¡{pokemon2.nombre} ha ganado la batalla!")