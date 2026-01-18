# Crear diccionario
diccionario = {'c1':'valor1','c2':'valor2'}

# Agregar otro valor al diccionario
diccionario['c3'] = 'valor3'

# Sobreescribir un valor existente
diccionario['c2'] = 'VALOR2'

# Ver claves, valores y pares clave-valor
print(diccionario)
print(diccionario.keys())    # Todas las claves
print(diccionario.values())  # Todos los valores
print(diccionario.items())   # Claves y valores

# Acceder al contenido de una clave
resultado = diccionario['c1']
print(resultado)

# Ejemplo con datos de un cliente
cliente = {'nombre': 'juan', 'apellido': 'fuentes', 'peso': 88}
consulta = cliente['apellido']
print(consulta)

# Diccionario con lista y otro diccionario dentro
diccionario2 = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(diccionario2['c2'][1])      # Acceder al segundo elemento de la lista
print(diccionario2['c3']['s2'])   # Acceder al valor de la clave 's2'


