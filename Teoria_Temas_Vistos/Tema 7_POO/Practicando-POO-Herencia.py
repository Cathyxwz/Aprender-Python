# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — HERENCIA

# Clase base (padre)
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")

    def hablar(self):
        print("El animal ha hablado")

# Clase derivada (hija) que hereda de Animal
class Pajaro(Animal):
    # Constructor extendido con nuevos parámetros
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)   # hereda atributos de Animal
        self.altura_vuelo = altura_vuelo

    # Nuevo método propio de Pajaro
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros")

# Crear objetos
simba = Animal(12, "Negro")
piolin = Pajaro(2, "Amarillo", 12)

# Usar métodos heredados y propios
piolin.nacer()
piolin.volar(12)

# HERENCIA MÚLTIPLE
class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja, Ja, ja")

    def hablar(self):
        print("Qué tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.reir()    # método heredado de Madre
mi_nieto.hablar()  # resolución de herencia: usa Padre primero
