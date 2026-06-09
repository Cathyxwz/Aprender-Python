# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — MÉTODOS

class Pollo:
    # Atributo de clase
    alas = True

    # Constructor con atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Método que hace que el pollo pía
    def piar(self):
        print("Pio")

    # Método que hace que el pollo vuele cierta distancia
    def volar(self, metros):
        print(f"El pollo ha volado {metros} metros")

    @classmethod #no puede accesder a metodos instancia
    def poner_huevo(cls,cantidad):
        print(f"Ponemos {cantidad} huevos") #no necesita self

# Crear objeto Pollo
mi_Pollo = Pollo("Amarillo", "Pollo")

# Usar métodos del objeto
mi_Pollo.piar()
mi_Pollo.volar(10)
mi_Pollo.poner_huevo(10)

