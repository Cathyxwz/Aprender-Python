# min y max → devuelven el menor y mayor valor de un iterable o conjunto de datos

# Valores directos
menor = min(58,34,7,50,97,81)
mayor = max(58,34,7,50,97,81)
print(menor, mayor)

# En listas
lista = [8,51,3,71,50]
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

# En listas de strings (orden alfabético)
nombres = ['Luisa', 'Cathy', 'Sara']
print(min(nombres), max(nombres))

# En strings (orden por caracteres)
nombre = 'Luis'
print(min(nombre), max(nombre))

# En diccionarios (valores)
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(min(diccionario.values()))
