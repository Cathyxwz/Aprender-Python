# Comprensión de listas → forma rápida y eficiente de crear listas en una sola línea

# Crear lista a partir de un string
palabra = "python"
lista = [letra for letra in palabra]
print(lista)   # ['p','y','t','h','o','n']

# Otra forma directa
lista2 = [letra for letra in "Python"]
print(lista2)

# Condicional dentro de la comprensión
lista3 = [n if n*2 > 10 else "no" for n in range(0,21,2)]
print(lista3)

# Ejemplo práctico: convertir pies a metros
pies = [10, 20, 30, 40, 50]
metros = [p/3.281 for p in pies]
print(metros)
