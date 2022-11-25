from caballosCarreras.control.access_db import AccessDB
from caballosCarreras.modelo.apostante import Apostante
from caballosCarreras.modelo.caballo import Caballo
from caballosCarreras.modelo.gran_premio import GranPremio
from utils.ioHandler import IOHandler
import utils.customLogs as logs
import logging
import random


def realizar_apuestas():
    """Cada apostante selecciona una cantidad a apostar y un caballo, ambos se guardan en una propiedad"""
    for apostante in apostantes:
        if apostante.saldo > 0:
            input_saldo = random.randint(1, 200)
            while input_saldo > apostante.saldo:
                input_saldo = random.randint(1, 200)
            input_caballo = random.choice([c.nombre for c in caballos_participantes])
            apostante.saldo_apostado = input_saldo
            apostante.caballo_apostado = input_caballo
            apostante.saldo -= input_saldo
            logs.info(f"El apostante: {apostante.nombre} ha apostado {input_saldo} por el caballo {input_caballo}")


def realizar_carreras():
    """Los caballos participantes van aumentando su avance hasta llegar a la distancia, si hay varios ganadores \
    se comprueba cual tiene mayor distancia, por ultimo se vuelve a 0 la distancia recorrida de cada caballo"""
    caballos_ganadores = []
    complete = False

    while not complete:
        for c in caballos_participantes:
            c.dist_recorrida += c.calcular_avance()
            if c.dist_recorrida >= gran_premio.distancia:
                caballos_ganadores.append(c)
                complete = True

    ganador = caballos_ganadores[0]

    for c in caballos_ganadores:
        if c.dist_recorrida > ganador.dist_recorrida:
            ganador = c

    logs.info(f"{ganador} ha ganado")

    for c in caballos_participantes:
        c.dist_recorrida = 0

    return ganador


def realizar_incrementos_postcarrera(ganador):
    """Se comprueba que el caballo elegido por el apostante sea el ganador entonces se realiza la suma y se resetea \
    el saldo apostado y caballo elegido de cada uno, se suma experiencia a los caballos y se actualiza la DB"""
    for apostante in apostantes:
        if apostante.caballo_apostado == ganador.nombre:
            incremento = apostante.incrementar_saldo(ganador.valor_apuesta)
            logs.info(f"El apostante {apostante.nombre} ha ganado {incremento}, ahora tiene un saldo de {apostante.saldo}")
        apostante.saldo_apostado = 0
        apostante.caballo_apostado = ""
        accessDB.actualizar_apostantes(apostante)

    for caballo in caballos_participantes:
        caballo.experiencia += 1
        accessDB.actualizar_caballos(caballo)
    ganador.experiencia += 4
    accessDB.actualizar_caballos(ganador)


if __name__ == "__main__":
    logs.setupLogging(logging.INFO, "../logs/caballos.log")
    accessDB = AccessDB()

    caballos = []
    apostantes = []
    grandes_premios = []

    with IOHandler('ficheros/caballos.txt', 'r') as archivo:
        for index, line in enumerate(archivo):
            lista = line.split("|")
            newCaballo = Caballo(index+1, lista[0], lista[1], int(lista[2]), int(lista[3]), int(lista[4]), int(lista[5]))
            caballos.append(newCaballo)
            # accessDB.insertar_caballos(newCaballo)

    with IOHandler('ficheros/apostantes.txt', 'r') as archivo:
        for index, line in enumerate(archivo):
            lista = line.split("|")
            newApostante = Apostante(index+1, lista[0], int(lista[1]))
            apostantes.append(newApostante)
            # accessDB.insertar_apostantes(newApostante)

    with IOHandler('ficheros/grandes_premios.txt', 'r') as archivo:
        for index, line in enumerate(archivo):
            lista = line.split("|")
            newGranpremio = GranPremio(index+1, lista[0], int(lista[1]), int(lista[2]))
            grandes_premios.append(newGranpremio)
            # accessDB.insertar_grandes_premios(newGranpremio)

    for gran_premio in grandes_premios:
        for i in range(gran_premio.num_carreras):
            logs.info(f"Gran premio: {gran_premio.nombre}, con distancia {gran_premio.distancia}, carrera numero {i+1}")

            caballos_participantes = list(filter(lambda caballo: caballo.id_granpremio == gran_premio.idd, caballos))

            realizar_apuestas()
            caballo_ganador = realizar_carreras()
            realizar_incrementos_postcarrera(caballo_ganador)

    accessDB.close()
