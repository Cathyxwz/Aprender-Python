# El ejercicio pide crear un programa que calcule la comisión del 13% de las ventas de un vendedor
# Primero debe preguntar el nombre del vendedor y el total de ingresos del mes
# Se usa input() para recibir los datos del usuario
# Como los ingresos llegan como texto, se convierten a float para poder hacer operaciones
# Se calcula la comisión multiplicando los ingresos por 13 y dividiendo entre 100
# Se usa round() para redondear el resultado a 2 decimales
# Finalmente se muestra en pantalla el nombre del vendedor y el monto de su comisión usando f-strings

nombre = input("Dime tu nombre: ")
ingresos = float(input("Dime tus ingresos: "))
comision = round(ingresos*13/100, 2)
print(f"Su nombre es: {nombre} y la comisión de sus ingresos es {comision}")
