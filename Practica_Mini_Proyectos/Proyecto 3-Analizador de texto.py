# El ejercicio pide crear un programa que analice un texto ingresado por el usuario.
# Primero se solicita un texto completo (frase, párrafo, poema, etc.).
# Luego se piden tres letras a elección del usuario.
# A partir de esa información, el programa debe mostrar:
# 1. Cuántas veces aparece cada una de las letras elegidas en el texto.
# 2. Cuántas palabras tiene el texto en total.
# 3. Cuál es la primera y cuál es la última letra del texto.
# 4. Cómo quedaría el texto si se invierte el orden de las palabras.
# 5. Si la palabra "Python" aparece dentro del texto.
#
# Se usan funciones y métodos básicos de Python:
# - input() para pedir datos al usuario
# - lower() para normalizar mayúsculas/minúsculas
# - count() para contar ocurrencias
# - split() y len() para contar palabras
# - indexación [0] y [-1] para primera y última letra
# - reverse() y join() para invertir palabras
# - in para verificar si "Python" está presente


# 1. Pedir texto al usuario
texto = input("Introduce tu texto: ")
print("Su texto es el siguiente:", texto)

# Pasar todo a minúsculas para evitar problemas con mayúsculas/minúsculas
texto_minus = texto.lower()

# 2. Pedir tres letras al usuario (sin usar for)
letra1 = input("Elige la primera letra: ").lower()
letra2 = input("Elige la segunda letra: ").lower()
letra3 = input("Elige la tercera letra: ").lower()

letras = [letra1, letra2, letra3]
print("Las letras que eligió son:", letras)

# --- Análisis ---

# 1. Contar cuántas veces aparece cada letra
print(f"La letra '{letra1}' aparece {texto_minus.count(letra1)} veces en el texto.")
print(f"La letra '{letra2}' aparece {texto_minus.count(letra2)} veces en el texto.")
print(f"La letra '{letra3}' aparece {texto_minus.count(letra3)} veces en el texto.")

# 2. Contar cuántas palabras hay en el texto
palabras = texto.split()
print("El número de palabras que tiene su texto es:", len(palabras))

# 3. Mostrar primera y última letra del texto
primer_letra = texto[0]
ultima_letra = texto[-1]
print("La primera letra de su texto es:", primer_letra)
print("La última letra de su texto es:", ultima_letra)

# 4. Invertir el orden de las palabras
palabras.reverse()
texto_invertido = " ".join(palabras)
print("Su texto con las palabras en orden inverso es:", texto_invertido)

# 5. Verificar si la palabra 'Python' está en el texto
contiene_python = "python" in texto_minus
print("¿La palabra 'Python' se encuentra en el texto?:", contiene_python)
