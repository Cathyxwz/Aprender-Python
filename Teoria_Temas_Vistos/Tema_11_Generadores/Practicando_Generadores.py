# FUNCIONES GENERADORAS EN PYTHON

# Función normal: devuelve una lista completa
def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista

# Función generadora: devuelve valores uno a uno con yield
def mi_generador():
    for x in range(1, 5):
        yield x * 10

# Comparación
print(mi_funcion())     # devuelve lista completa
print(mi_generador())   # devuelve objeto generador

# Uso de next() para obtener valores del generador
g = mi_generador()
print(next(g))          # primer valor
print(next(g))          # segundo valor
