# ARCHIVOS EN PYTHON
# Ejemplo: abrir, leer e iterar un archivo

# Abrir archivo en modo lectura
mi_archivo = open("prueba.txt")

# Leertodo el contenido del archivo
print(mi_archivo.read())

# Iterar línea por línea en el archivo
for l in mi_archivo:
    print("Aquí dice: " + l)

# Convertir todas las líneas en una lista
todas = mi_archivo.readlines()
print(todas)

# Cerrar archivo
mi_archivo.close()
