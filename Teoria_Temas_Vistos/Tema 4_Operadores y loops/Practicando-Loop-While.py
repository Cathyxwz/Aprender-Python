# Loop while → se ejecuta mientras la condición sea verdadera

monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1   # anticipado
else:
    print("No tengo más dinero")

# Ejemplo con entrada del usuario
respuesta = 's'
while respuesta == 's':
    respuesta = input("¿Quieres seguir? (s/n)")   # sin anticipar
else:
    print("Gracias")

# Uso de pass → marcador de posición
pass1 = 's'
while pass1 == 's':
    pass
print("Gracias")

# Uso de break → interrumpe el bucle
nombre = "carro"
for letra in nombre:
    if letra == "r":
        break
    print(letra)

# Uso de continue → salta una iteración
nombre2 = "carro"
for letra in nombre2:
    if letra == "r":
        continue
    print(letra)
