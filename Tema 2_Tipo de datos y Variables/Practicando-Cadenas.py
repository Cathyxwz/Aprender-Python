# Formateo de cadenas usando .format(): se colocan {} como marcadores y luego se reemplazan con valores
x = 10
y = 5
print("Mis numeros son {} y {}".format(x, y))

# También con .format() se pueden incluir operaciones dentro del texto
print("La suma de {} y {} es igual a {}".format(x, y, x + y))

# Formateo de cadenas usando f-strings: se escribe f"" y dentro de {} se insertan variables directamente
color = "Rojo"
matricula = 541623
print(f"El auto es {color} y su matricula es {matricula}")

