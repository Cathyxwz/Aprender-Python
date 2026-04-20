# ARGUMENTOS - ARGS
# Ejemplo 1: suma de varias cosas

# Definimos una función que recibe un número indefinido de argumentos
def suma(*args):
    # La función sum() suma todos los valores recibidos en args
    return sum(args)
print(suma(1, 2, 7, 8, 9))  # Resultado: 27


# Ejemplo 2: función que retorna la suma de los cuadrados
def suma_cuadrados(*args):
    total = 0
    for n in args:
        total += n ** 2
    return total


# Ejemplo 3: función que suma valores absolutos (convierte negativos a positivos)
def suma_absolutos(*args):
    total = 0
    for n in args:
        total += abs(n)
    return total


# Ejemplo 4: función que recibe un nombre y varios números
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"
