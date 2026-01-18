# Crear listas
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']

# Concatenar listas con variables
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

# Las listas pueden contener distintos tipos de datos
otra_lista = ['hola', 55, 6.1]

# Sobreescribir un elemento de la lista
mi_lista3[0] = 'alfa'

# Agregar un elemento al final de la lista
mi_lista3.append('g')

# Eliminar un elemento de la lista (por índice)
mi_lista3.pop(0)   # elimina el primer elemento
print(mi_lista3)

# Concatenar listas directamente en print
print(mi_lista + mi_lista2)

# Ver un elemento por índice
resultado2 = mi_lista[0]
print(resultado2)

# Ordenar listas
mi_lista4 = ['g','s','a','m','r']
mi_lista4.sort()      # ordena de a-z
mi_lista4.reverse()   # invierte el orden (z-a)
print(mi_lista4)
