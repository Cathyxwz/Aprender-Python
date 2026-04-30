# IMPORTAR MÓDULO OS Y PATH

import os
# Cambiar la ruta de trabajo actual
os.chdir("C:\\Users\\kathe\\Downloads\\Otra_ruta")
# Abrir y leer un archivo en la nueva ruta
archivo = open("Otro_texto.txt")
print(archivo.read())
archivo.close()

# Crear una nueva carpeta desde Python en el ordenador
os.makedirs("C:\\Users\\kathe\\Downloads\\Otra_ruta\\otra")

# Ejemplo de manipulación de rutas
ruta = "C:\\Users\\kathe\\OneDrive\\Documentos\\Python-2026\\Teoria_Temas_Vistos\\Tema 6_Archivos\\Prueba.txt"

# Obtener solo el nombre del archivo
archivo = os.path.basename(ruta)
print(archivo)
# Obtener solo el directorio
directorio = os.path.dirname(ruta)
print(directorio)
# Separar nombre y extensión
mi_ruta = os.path.splitext(ruta)
print(mi_ruta)

# Eliminar carpeta creada
os.rmdir("C:\\Users\\kathe\\Downloads\\Otra_ruta\\otra")

# Uso de pathlib para rutas multiplataforma (Windows/Mac/Linux)
from pathlib import Path
carpeta = Path("C:\\Users\\kathe\\Downloads\\Otra_ruta") / "Otro_texto.txt"
archivo = open(carpeta, "r")
print(archivo.read())
archivo.close()
