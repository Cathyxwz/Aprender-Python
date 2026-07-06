# DECORADORES: funciones que modifican el comportamiento de otras funciones

# Ejemplo: decorar una función
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        print(funcion(palabra))
        print("Adiós")
    return otra_funcion

@decorar_saludo
def mayusculas(texto):
    return texto.upper()

@decorar_saludo
def minusculas(texto):
    return texto.lower()

# Ejecutar funciones decoradas
mayusculas("Python")
minusculas("Python")


