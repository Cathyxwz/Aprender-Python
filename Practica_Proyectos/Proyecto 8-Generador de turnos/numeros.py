def decorar_turno(funcion):
    def envolver():
        print("\n" + "-" * 30)
        print("Su turno es:")
        print(funcion())
        print("Aguarde y será atendido")
        print("-" * 30 + "\n")

    return envolver


def generador_turnos(letra):
    numero = 1

    while True:
        yield f"{letra}-{numero}"
        numero += 1


turnos_perfumeria = generador_turnos("P")
turnos_farmacia = generador_turnos("F")
turnos_cosmeticos = generador_turnos("C")


@decorar_turno
def dar_turno_perfumeria():
    return next(turnos_perfumeria)


@decorar_turno
def dar_turno_farmacia():
    return next(turnos_farmacia)


@decorar_turno
def dar_turno_cosmeticos():
    return next(turnos_cosmeticos)
