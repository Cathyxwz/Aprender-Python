# Condicionales en Python

# if → ejecuta código si la condición es verdadera
if 10 > 9:
    print('Es correcto')   # Se cumple, imprime "Es correcto"

# if + else → ejecuta una opción si se cumple y otra si no
if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')   # Se ejecuta porque la condición es falsa

# if + elif + else → varias condiciones encadenadas
mascota = 'perro'
if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
else:
    print('no tienes un gato')

# Condicionales anidados
edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres mayor de edad')


