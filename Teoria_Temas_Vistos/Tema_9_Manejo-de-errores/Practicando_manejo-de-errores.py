# PROGRAMACIÓN ORIENTADA A OBJETOS (POO) — MANEJO DE ERRORES

# Ejemplo 1: uso de try-except-else-finally
def al_cuadrado():
    numero = int(input("Ingrese un número: "))
    resultado = numero * numero
    print(f"El cuadrado de {numero} es {resultado}")

try:
    al_cuadrado()
except ValueError:
    print("Ese no es un número")
except Exception:
    print("Hay un error interno")
else:
    print("El cuadrado se calculó correctamente")
finally:
    print("Gracias por calcular el cuadrado")


# Ejemplo 2: validación en bucle
def pedir_numero():
    while True:
        try:
            numero2 = int(input("Ingrese un número: "))
            print("Ingresaste el número", numero2)
            return numero2
        except ValueError:
            print("Ese no es un número")

# Ejecutar función
pedir_numero()
