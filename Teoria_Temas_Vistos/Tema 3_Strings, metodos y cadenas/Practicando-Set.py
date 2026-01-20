# Los sets:
# - No permiten elementos repetidos
# - No están ordenados por índices
# - Son inmutables en cuanto a estructura (no se accede por índice)
# - No pueden incluir listas ni diccionarios, pero sí tuples

mi_set = set([1, 2, 3, 4, 5])
print(mi_set)

# Consultar si un elemento está en el set
print(2 in mi_set)   # Resultado: True

# Crear sets
s1 = {1, 2, 3}
s2 = {4, 5, 6}

# Añadir un elemento
s1.add(0)

# Remover un elemento
s1.remove(0)

# Unir dos sets
s3 = s1.union(s2)
print(s3)
