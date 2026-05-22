# Proyecto: Juego de adivinanza de números
# El programa pide el nombre del usuario y le da 8 intentos para adivinar un número secreto entre 1 y 100.
# Responde según la elección del usuario: fuera de rango, menor, mayor o correcto.

import random

# Pedir nombre al usuario
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}, he pensado un número del 1 al 100. Tienes 8 intentos para adivinarlo.")

# Generar número secreto aleatorio
numero_adivinar = random.randint(1, 100)
intentos = 8

# Bucle de intentos
for intento in range(1, intentos + 1):
    numero_usuario = int(input(f"Intento {intento}: Ingresa un número: "))

    # Validar rango permitido
    if numero_usuario < 1 or numero_usuario > 100:
        print("El número no está permitido. Debe estar entre 1 y 100.")
    # Número menor al secreto
    elif numero_usuario < numero_adivinar:
        print("Incorrecto. Has elegido un número menor al número secreto.")
    # Número mayor al secreto
    elif numero_usuario > numero_adivinar:
        print("Incorrecto. Has elegido un número mayor al número secreto.")
    # Número correcto
    else:
        print(f"¡Correcto, {nombre}! Has ganado en {intento} intentos.")
        break
# Si no acierta en los 8 intentos
else:
    print(f"Lo siento, {nombre}. Se acabaron los intentos. El número secreto era {numero_adivinar}.")
