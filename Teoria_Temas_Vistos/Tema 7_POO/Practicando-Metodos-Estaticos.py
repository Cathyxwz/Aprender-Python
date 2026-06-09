# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — MÉTODOS ESTÁTICOS

class Pollo:
    # Atributo de clase
    alas = True

    # Método estático → no depende de atributos ni de instancias
    @staticmethod
    def mirar():
        print("Mirando")

# Llamar directamente al método estático desde la clase
Pollo.mirar()

