# Proyecto: Interacción entre funciones
# Ejemplo: elegir un palito, el más corto lava los platos

from random import shuffle

# Lista inicial de palitos
palitos = ["-", "--", "---", "----"]

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# Pedir al usuario que elija un número
def probar_suerte():
    intento = ""
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un número del 1 al 4: ")
    return int(intento)

# Comprobar el intento del usuario
def chequear_intento(lista, intento):
    seleccion = intento - 1
    if lista[seleccion] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te salvaste")
    print(f"Te ha tocado {lista[seleccion]}")

# Funcionar todas las funciones juntas
palitos_mezclados = mezclar(palitos)
numero_elegido = probar_suerte()
chequear_intento(palitos_mezclados, numero_elegido)

# Ejemplo 2: lanzar dos dados y evaluar jugada
from random import randint
def lanzar_dados():
    # Genera dos números aleatorios entre 1 y 6
    resultado1 = randint(1, 6)
    resultado2 = randint(1, 6)
    return resultado1, resultado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:  # suma_dados >= 10
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Usar las funciones de dados
d1, d2 = lanzar_dados()
mensaje = evaluar_jugada(d1, d2)
print(f"Dados: {d1}, {d2}")
print(mensaje)


#Ejemplo 3: Funciones dinámicas con listas y cálculos
lista_numeros = [1, 3, 6, 6, 7, 87, 10]
# Función para reducir lista:
# - elimina duplicados
# - elimina el valor más alto
def reducir_lista(lista):
    # Eliminar duplicados convirtiendo a set
    lista_sin_duplicados = list(set(lista))
    # Eliminar el valor más alto
    lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return lista_sin_duplicados

# Función para calcular promedio de una lista
def promedio(lista):
    return sum(lista) / len(lista)

# Ejemplo de uso
lista_reducida = reducir_lista(lista_numeros)
print("Lista reducida:", lista_reducida)
print("Promedio de la lista reducida:", promedio(lista_reducida))

# Ejemplo4: lanzar una moneda y decidir qué hacer con una lista

from random import choice

# Función que devuelve al azar "Cara" o "Cruz"
def lanzar_moneda():
    return choice(["Cara", "Cruz"])

# Función que decide qué hacer con la lista según el resultado de la moneda
def probar_suerte(resultado_moneda, lista):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []  # lista vacía
    else:  # resultado_moneda == "Cruz"
        print("La lista fue salvada")
        return lista

# Ejemplo de lista
lista_numeros = [3, 7, 12, -5, 20]

# Uso de las funciones
resultado = lanzar_moneda()
lista_final = probar_suerte(resultado, lista_numeros)
print("Resultado de la moneda:", resultado)
print("Lista final:", lista_final)

