# Loop for → se usa cuando sabemos cuántas veces se repetirá el bucle y es iterable

# Recorrer lista
lista = ['a', 'b', 'c']
for letra in lista:
    print(letra)

# Con condicionales
lista2 = ['pablo', 'laura', 'cathy', 'luis']
for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("No empieza con l:", nombre)

# Sumar elementos de una lista
numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor)   # Resultado: 15

# Recorrer string
palabra = 'python'
for letra in palabra:
    print(letra)

# Desempaquetar listas dentro de lista
for a, b in [[1, 2], [2, 3], [4, 5]]:
    print(a, b)

# Recorrer diccionario
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for clave, valor in dic.items():
    print(clave, valor)
