# ARGUMENTOS - KWARGS
# Ejemplo 1: combinación de argumentos normales, *args y **kwargs

def prueba(num1, num2, *args, **kwargs):
    # Mostrar los dos primeros valores obligatorios
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    # Recorrer los argumentos adicionales (args)
    for arg in args:
        print(f"Arg es igual a {arg}")

    # Recorrer los argumentos con nombre (kwargs)
    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")

# Lista y diccionario para probar la función
lista_args = [5, 6, 8, 12]
diccionario_args = {"x":3, "y":4, "z":5}

# Llamada a la función con *args y **kwargs
prueba(5, 11, *lista_args, **diccionario_args)


# Ejemplo 2: describir persona con atributos dinámicos
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for atributo, valor in kwargs.items():
        print(f"{atributo}: {valor}")
