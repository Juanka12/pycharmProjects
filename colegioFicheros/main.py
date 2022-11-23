import colegioLogs
import logging
from ioHandler import IOHandler
from colegioClases import Colegio, Alumno
from functools import reduce


if __name__ == "__main__":
    colegioLogs.setupLogging(logging.INFO, "../logs/colegio.log")

    colegios = []
    with IOHandler('datos.txt', 'r') as archivo:
        colegioNombres = []
        for line in archivo:
            lista = line.rstrip().split("|")
            if lista[0] in colegioNombres:
                for colegio in colegios:
                    if colegio.nombre == lista[0]:
                        newAlumno = Alumno(lista[1], lista[2], lista[3], lista[4].split(";"))
                        colegio.addAlumno(newAlumno)
            else:
                colegioNombres.append(lista[0])
                colegios.append(Colegio(lista[0]))

    logging.info(colegios)

    for colegio in colegios:
        with IOHandler(f'{colegio}.txt', 'w') as archivo:
            for alumno in colegio.alumnos:
                archivo.write(str(alumno)+"\n")
