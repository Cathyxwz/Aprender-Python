# Pasar todos los caracteres a mayúsculas (UPPER)
texto = "Este es el texto de Catherine"
resultado = texto.upper() # Convierte todo el string a mayúsculas
resultado2 = texto[2].upper() # Convierte solo el carácter en índice 2 a mayúscula
print(resultado, resultado2)

# Pasar todos los caracteres a minúsculas (LOWER)
texto = "Este es el texto de Catherine"
resultado = texto.lower() # Convierte todo el string a minúsculas
print(resultado)

# Separar palabras (SPLIT)
texto = "Este es el texto de Catherine"
resultado = texto.split() # Separa el string en una lista de palabras
print(resultado)

# Unir palabras (JOIN)
a = "Aprender"
b = "Python"
c = "es"
d = "Genial"
e = " ".join([a, b, c, d]) # Une las palabras con un espacio en medio
print(e)

# Buscar posición de un carácter o subcadena (FIND)
texto = "Este es el texto de Catherine"
resultado = texto.find("e") # Devuelve la posición de la primera aparición de "e"
print(resultado)

# Reemplazar texto (REPLACE)
texto = "Este es el texto de Catherine"
resultado = texto.replace("Catherine", "todos") # Reemplaza "Catherine" por "todos"
print(resultado)
