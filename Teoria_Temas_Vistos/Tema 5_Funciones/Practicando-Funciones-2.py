# Función que encuentra el café más caro de una lista de tuplas (nombre, precio)

lista_Cafe = [("Capuchino", 2.3), ("Expreso", 1.20), ("Moka", 1.9)]

def encontrar_cafe_caro(lista):
    precio_mayor = 0
    cafe_mas_caro = ""
    for c, p in lista:        # recorrer cada tupla (café, precio)
        if p > precio_mayor:  # comparar precios
            precio_mayor = p
            cafe_mas_caro = c
    return (cafe_mas_caro, precio_mayor)  # devolver nombre y precio

print(encontrar_cafe_caro(lista_Cafe))   # ('Capuchino', 2.3)
