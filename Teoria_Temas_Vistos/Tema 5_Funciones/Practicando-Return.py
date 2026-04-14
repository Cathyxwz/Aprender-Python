# Funciones con return → devuelven un valor que puede usarse fuera de la función

# Multiplicar dos números
def multiplicar(numero1, numero2):
    # Devuelve el producto de dos números
    return numero1 * numero2

resultado = multiplicar(5, 10)
print(resultado)   # 50


# Dividir dos números
def dividir(numero3, numero4):
    # Devuelve el cociente de dos números
    return numero3 / numero4

numero3 = int(input("Introduce un número: "))
numero4 = int(input("Introduce otro número: "))
resultado = dividir(numero3, numero4)
print(resultado)

