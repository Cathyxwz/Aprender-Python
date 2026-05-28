# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — ATRIBUTOS

class Pajaro:
    # Atributo de clase → compartido por todos los objetos
    alas = True

    # Constructor con atributos de instancia
    def __init__(self, color, especie):
        # Atributos de instancia → propios de cada objeto
        self.color = color
        self.especie = especie

# Crear un objeto con atributos específicos
mi_Pajaro = Pajaro('rojo', 'Tucan')

# Acceder a los atributos del objeto
print(f"El color del pájaro es: {mi_Pajaro.color} y la especie es: {mi_Pajaro.especie}")
