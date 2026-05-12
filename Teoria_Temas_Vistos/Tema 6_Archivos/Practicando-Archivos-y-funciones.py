# FUNCIONES CON DOCUMENTOS
# Función 1: abrir y leer un archivo (modo "r")
def abrir_leer(nombre_archivo):
    archivo = open(nombre_archivo, "r")   # "r" → modo lectura
    contenido = archivo.read()            # leer txdo el contenido
    archivo.close()                       # cerrar archivo
    return contenido                      # devolver el texto leíd

# Función 2: sobrescribir un archivo (modo "w")
def sobrescribir(nombre_archivo):
    archivo = open(nombre_archivo, "w")   # "w" → modo escritura (borra contenido previo)
    archivo.write("contenido eliminado")  # escribir nuevo texto
    archivo.close()                       # cerrar archivo

# Función 3: registrar un error en un archivo (modo "a")
def registro_error(nombre_archivo):
    archivo = open(nombre_archivo, "a")   # "a" → modo agregar (append)
    archivo.write("se ha registrado un error de ejecución")  # añadir texto al final
    archivo.close()                       # cerrar archivo
