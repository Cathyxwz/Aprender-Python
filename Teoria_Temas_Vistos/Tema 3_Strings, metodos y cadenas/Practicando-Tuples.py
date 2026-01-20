# Los tuples son inmutables (no se pueden modificar directamente)
# Ocupan menos espacio en memoria que las listas

mi_tuple = (1, 2, "a", 0)   # Puede contener distintos tipos de datos

# Convertir un tuple en lista para poder modificarlo
mi_tuple = list(mi_tuple)
print(mi_tuple)

# Acceder a un elemento por índice
print(mi_tuple[1])   # Resultado: 2

# Contar cuántas veces aparece un valor
print(mi_tuple.count(1))   # Resultado: 1

# Saber en qué índice está un valor
print(mi_tuple.index(2))   # Resultado: 1

