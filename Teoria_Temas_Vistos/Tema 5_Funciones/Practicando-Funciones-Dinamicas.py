# Funciones dinámicas → trabajan con listas y loops para procesar datos

mi_lista = [55, 999, 1000]

# Función que revisa qué números tienen 3 cifras
def chequear_3_cifras(lista):
    lista_3_cifras = []  # lista vacía para guardar resultados
    for l in lista:      # recorrer cada elemento
        if l in range(100, 1000):   # condición: número entre 100 y 999
            lista_3_cifras.append(l)  # agregar a la nueva lista
    return lista_3_cifras  # devolver lista final

# Llamar la función y mostrar resultado
resultado = chequear_3_cifras(mi_lista)
print(resultado)   # [999]

