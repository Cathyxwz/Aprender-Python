# PATHLIB — manejo moderno de rutas en Python

from pathlib import Path

# Definir la ruta de un archivo
carpeta = Path("C:\\Users\\kathe\\OneDrive\\Documentos\\Python-2026\\Teoria_Temas_Vistos\\Tema 6_Archivos\\Prueba.txt")

# Leer contenido del archivo directamente
print(carpeta.read_text())

# Obtener solo el nombre del archivo
print(carpeta.name)

# Obtener la extensión del archivo
print(carpeta.suffix)

# Obtener el nombre del archivo sin extensión
print(carpeta.stem)

# Verificar si el archivo existe
if not carpeta.exists():
    print("No existe")
else:
    print("Sí existe")


