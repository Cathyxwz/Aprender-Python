# PROYECTO: Gestor de Recetas
# Permite leer, crear y eliminar recetas y categorías dentro de una carpeta.

import os
import shutil

# Ruta principal donde se guardan las recetas
RUTA = "C:\\Users\\kathe\\OneDrive\\Documentos\\Python-2026\\Practica_Mini_Proyectos\\Recetas"

# Contar todas las recetas en la carpeta
def contar_recetas():
    return sum(len(archivos) for _, _, archivos in os.walk(RUTA))

# Mostrar bienvenida y estado inicial
def mostrar_bienvenida():
    os.system("cls")  # limpiar pantalla
    print(f"""Hola, bienvenid@.
Tu carpeta de recetas se encuentra en: {RUTA}
Tienes {contar_recetas()} recetas en total.
""")

# Elegir categoría
def elegir_categoria():
    categorias = sorted(c for c in os.listdir(RUTA) if os.path.isdir(os.path.join(RUTA, c)))
    for numero, categoria in enumerate(categorias, 1):
        print(f"{numero}. {categoria}")
    eleccion = input("Elige una categoria: ")
    if eleccion.isnumeric() and 1 <= int(eleccion) <= len(categorias):
        return categorias[int(eleccion) - 1]
    print("Categoria invalida.")
    return None

# Elegir receta dentro de una categoría
def elegir_receta(categoria):
    ruta_categoria = os.path.join(RUTA, categoria)
    recetas = sorted(r for r in os.listdir(ruta_categoria) if r.endswith(".txt"))
    for numero, receta in enumerate(recetas, 1):
        print(f"{numero}. {receta}")
    eleccion = input("Elige una receta: ")
    if eleccion.isnumeric() and 1 <= int(eleccion) <= len(recetas):
        return recetas[int(eleccion) - 1]
    print("Receta invalida.")
    return None

# Leer receta
def leer_receta():
    categoria = elegir_categoria()
    receta = elegir_receta(categoria)
    archivo = os.path.join(RUTA, categoria, receta)
    with open(archivo, "r", encoding="utf-8") as texto:
        print("\n" + texto.read())

# Crear receta
def crear_receta():
    categoria = elegir_categoria()
    nombre = input("Nombre de la nueva receta: ").strip()
    contenido = input("Contenido de la receta: ")
    if not nombre.endswith(".txt"):
        nombre += ".txt"
    archivo = os.path.join(RUTA, categoria, nombre)
    with open(archivo, "w", encoding="utf-8") as texto:
        texto.write(contenido)
    print("Receta creada correctamente.")

# Crear categoría
def crear_categoria():
    nombre = input("Nombre de la nueva categoria: ").strip()
    os.makedirs(os.path.join(RUTA, nombre), exist_ok=True)
    print("Categoria creada correctamente.")

# Eliminar receta
def eliminar_receta():
    categoria = elegir_categoria()
    receta = elegir_receta(categoria)
    if not receta:
        return
    os.remove(os.path.join(RUTA, categoria, receta))
    print("Receta eliminada correctamente.")

# Eliminar categoría
def eliminar_categoria():
    categoria = elegir_categoria()
    shutil.rmtree(os.path.join(RUTA, categoria))
    print("Categoria eliminada correctamente.")

# Menú principal
opcion = "0"
while opcion != "6":
    mostrar_bienvenida()
    print("""Elige una de las siguientes opciones:
1. Leer receta
2. Crear receta
3. Crear categoria
4. Eliminar receta
5. Eliminar categoria
6. Finalizar""")

    opcion = input("Tu opcion: ")

    if opcion == "1":
        leer_receta()
    elif opcion == "2":
        crear_receta()
    elif opcion == "3":
        crear_categoria()
    elif opcion == "4":
        eliminar_receta()
    elif opcion == "5":
        eliminar_categoria()
    elif opcion == "6":
        print("Programa finalizado.")
    else:
        print("Opcion invalida.")

    if opcion != "6":
        input("\nPresiona cualquier tecla para volver al menu...")
