# Conversión implícita: al sumar un entero con un float, el resultado se convierte automáticamente en float
num1 = 20
num2 = 30.5
num1 = num1 + num2
print(type(num1))
print(type(num2))

# Conversión explícita: se transforma un float en entero usando int()
num1 = 5.8
print(num1)
print(type(num1))
num2 = int(num1)
print(num2)
print(type(num2))

# Ejemplo práctico: se pide la edad con input(), se convierte a entero y se suma 1
edad = input("Introduce tu edad: ")
edad = int(edad)
nueva_edad = edad + 1
print(nueva_edad)



