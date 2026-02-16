# random → funciones para generar valores aleatorios
from random import *

# Número entero aleatorio entre 1 y 10
aleatorio = randint(1, 10)
print(aleatorio)

# Número decimal aleatorio entre 1 y 10 (redondeado)
aleatorio2 = round(uniform(1, 10))
print(aleatorio2)

# Número decimal aleatorio entre 0 y 1
aleatorio3 = random()
print(aleatorio3)

# Elegir un elemento aleatorio de una lista
colores = ['azul', 'rojo','amarillo','verde']
aleatorio4 = choice(colores)
print(aleatorio4)

# Desordenar una lista
numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)


