# EJERCICIO 1: devolver_distintos
# Recibe 3 enteros y devuelve:
# - el mayor si la suma > 15
# - el menor si la suma < 10
# - el intermedio si la suma está entre 10 y 15
def devolver_distintos(a, b, c):
    resultado = a + b + c
    if resultado > 15:
        return max(a, b, c)
    elif resultado < 10:
        return min(a, b, c)
    else:
        numeros = sorted([a, b, c])
        return numeros[1]

print("Respuesta final:", devolver_distintos(5, 11, 8))


# EJERCICIO 2: letras únicas ordenadas
# Recibe una palabra y devuelve sus letras únicas en orden alfabético
def ordenar_palabra(palabra):
    letras_unicas = set(palabra)
    return sorted(letras_unicas)

print("Letras únicas ordenadas:", ordenar_palabra("programacion"))


# EJERCICIO 3: detectar repetidos consecutivos
# Recibe cantidad indefinida de argumentos y devuelve True si hay dos iguales seguidos
def tiene_repetidos(*args):
    for i in range(len(args) - 1):
        if args[i] == args[i+1]:
            return True
    return False

print(tiene_repetidos(5, 11, 8, 9, 10, 10))


# EJERCICIO 4: contar primos
# Recibe un número y devuelve cuántos primos hay hasta ese número
def contar_primos(numero):
    if numero < 2:
        return 0
    primos = []
    for n in range(2, numero + 1):
        es_primo = True
        for divisor in range(2, n):
            if n % divisor == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    print("Primos:", primos)
    return len(primos)

print("Cantidad:", contar_primos(20))

