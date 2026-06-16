# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — HERENCIA

# Clase base (padre)
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")

# Clase derivada (hija) que hereda de Animal
class Pajaro(Animal):
    pass  # no agrega nada nuevo, pero hereda tdo de Animal

# Crear objeto Pajaro
piolin = Pajaro(2, "Amarillo")

# Usar métdo heredado de Animal
piolin.nacer()


