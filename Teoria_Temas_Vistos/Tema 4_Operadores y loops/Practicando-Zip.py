# zip → combina elementos de varios iterables en tuplas

nombres = ['Ana', 'Hugo', 'Maria']
edades = [5, 6, 10]
ciudades = ['España', 'Mexico', 'Colombia']

# Crear lista de tuplas con zip
combinados = list(zip(nombres, edades, ciudades))
print(combinados)   # [('Ana',5,'España'), ('Hugo',6,'Mexico'), ('Maria',10,'Colombia')]

# Recorrer los elementos combinados
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
