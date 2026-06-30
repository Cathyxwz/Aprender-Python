# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — POLIMORFISMO

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Muu!")

# Usa el mismo nombre de métdo en diferentes clases
class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        for n in range(0, 3):
            print(f"Beee {n+1}")

# Crear objetos
vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

# Lista de animales
animales_granja = [vaca1, oveja1]

# Polimorfismo: mismo métdo 'hablar' con comportamientos distintos
for animal in animales_granja:
    animal.hablar()
