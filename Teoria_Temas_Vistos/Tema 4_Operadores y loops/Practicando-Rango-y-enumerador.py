#RANGO:
# range → genera una secuencia de números sin necesidad de crear una lista completa
# Usar range en un loop for
for numero in range(1,5):   # desde 1 hasta 4 (el límite superior no se incluye)
    print(numero)

# Crear lista a partir de range
lista = list(range(1,101))  # números del 1 al 100
print(lista)

#ENUMERADOR: solo iterables
# enumerate → devuelve pares (índice, valor) de un iterable
# Usar enumerate en un loop for
lista = ['a','b','c']
for item in enumerate(lista):
    print(item)   # imprime (0,'a'), (1,'b'), (2,'c')

# Convertir directamente en lista de tuplas
lista2 = ['a','b','c']
mis_tuples = list(enumerate(lista2))
print(mis_tuples)   # [(0,'a'), (1,'b'), (2,'c')]

#EJEMPLO ENUMERADOR CON LOOOP:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)

