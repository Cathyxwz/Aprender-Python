# PROYECTO: Juego del Ahorcado

from random import choice

# Lista de palabras posibles
palabras = ["panadero", "dinosaurio", "caballo", "tiburon"]

# Función para elegir una palabra al azar
def elegir_palabra(lista):
    return choice(lista)

# Función para mostrar el tablero con guiones y letras acertadas
def mostrar_tablero(palabra, letras_correctas, vidas):
    tablero = [l if l in letras_correctas else "_" for l in palabra]
    print(" ".join(tablero))
    print("Vidas:", vidas)

# Función principal del juego
def jugar():
    palabra = elegir_palabra(palabras)
    letras_correctas = []
    vidas = 6

    while vidas > 0:
        mostrar_tablero(palabra, letras_correctas, vidas)
        letra = input("Elige una letra: ").lower()

        # Validar si la letra está en la palabra
        if letra in palabra:
            letras_correctas.append(letra)
        else:
            vidas -= 1

        # Verificar si el jugador ha ganado
        if all(l in letras_correctas for l in palabra):
            print("¡Ganaste! La palabra era:", palabra)
            return

    # Si se acaban las vidas, el jugador pierde
    print("Perdiste. La palabra era:", palabra)

# Iniciar el juego
jugar()



