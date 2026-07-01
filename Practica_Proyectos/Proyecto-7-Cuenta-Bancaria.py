# PROYECTO: Sistema de Cuenta Bancaria

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Métdo especial para mostrar datos del cliente
    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellido}\n"
                f"Número de cuenta: {self.numero_cuenta}\n"
                f"Balance: {self.balance}")

    # Métdo para depositar dinero
    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Has depositado {cantidad}. Tu nuevo balance es {self.balance}.")

    # Métdo para retirar dinero con validación
    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Has retirado {cantidad}. Tu nuevo balance es {self.balance}.")
        else:
            print("No puedes retirar más dinero del que tienes.")


# Función para crear cliente
def crear_cliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingresa tu número de cuenta: ")
    balance_inicial = float(input("Ingresa tu balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance_inicial)


# Función principal
def inicio():
    cliente = crear_cliente()
    print("\nCliente creado exitosamente:")
    print(cliente)

    while True:
        print("""
Elige una de las siguientes opciones:
1. Depositar
2. Retirar
3. Salir
""")
        opcion = input("Tu opción: ")

        if opcion == "1":
            cantidad = float(input("Cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Aquí se ejecuta el programa
if __name__ == "__main__":
    inicio()
