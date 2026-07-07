from numeros import (
    dar_turno_cosmeticos,
    dar_turno_farmacia,
    dar_turno_perfumeria,
)

def sacar_otro_turno():
    while True:
        respuesta = input("¿Deseas sacar otro turno? (s/n): ").lower()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            return False
        else:
            print("Respuesta no válida. Escribe 's' o 'n'.")


def inicio():
    while True:
        print("""
Elige una de las siguientes areas:
1. Perfumeria
2. Farmacia
3. Cosmeticos
4. Salir
""")
        opcion = input("Tu opción: ")

        if opcion == "1":
            dar_turno_perfumeria()
            if not sacar_otro_turno():
                break

        elif opcion == "2":
            dar_turno_farmacia()
            if not sacar_otro_turno():
                break

        elif opcion == "3":
            dar_turno_cosmeticos()
            if not sacar_otro_turno():
                break

        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    inicio()
