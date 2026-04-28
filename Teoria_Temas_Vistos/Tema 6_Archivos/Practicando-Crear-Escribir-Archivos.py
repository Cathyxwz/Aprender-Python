# CREAR Y ESCRIBIR ARCHIVOS EN PYTHON

# Ejemplo 1: crear un nuevo archivo y escribir en él
archivo = open("prueba1.txt", "w")  # modo "w" crea el archivo si no existe
archivo.write("Soy una nueva línea")  # escribe texto dentro del archivo
archivo.close()  # cerrar archivo

# Ejemplo 2: sobrescribir contenido existente con nuevo texto
archivo = open("prueba.txt", "w")  # elimina contenido previo y escribe nuevo
lista = ["Hola", "mundo", "aqui", "estoy"]
archivo.writelines(lista)  # escribe varios strings concatenados
archivo.close()

# Ejemplo 3: agregar texto al final de un archivo existente
archivo = open("prueba.txt", "a")  # modo "a" agrega contenido sin borrar lo anterior
archivo.write("Soy otra línea de texto")  # añade nueva línea
archivo.close()
