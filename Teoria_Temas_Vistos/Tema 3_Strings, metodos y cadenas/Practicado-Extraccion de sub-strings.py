# Extraer desde índice 2 hasta el 5 (no incluye el 5)
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)   # Resultado: "CDE"

# Si se deja vacío después de :, extrae desde el índice 2 hasta el final
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:]
print(fragmento)   # Resultado: "CDEFGHIJKLM"

# Si se deja vacío al inicio, extrae desde el inicio hasta el índice 5 (sin incluirlo)
texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]
print(fragmento)   # Resultado: "ABCDE"

# Tercer factor: cada cuántos caracteres se extrae
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)   # Resultado: "CEG"

# Si se pone un número negativo en el paso, recorre al revés
texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1]
print(fragmento)   # Resultado: "MLKJIHGFEDCBA"
