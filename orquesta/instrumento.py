from abc import ABC
import random
import orquestLogs
from badTunedException import BadTunedException


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.afinado = False

    def funcion_logs(func):
        def closure(self):
            orquestLogs.info(f'Afinando {self.nombre}')
            resultado = func(self)
            orquestLogs.info(f'Afinado: {resultado}')
        return closure

    @funcion_logs
    def afinar(self):
        if random.randint(0, 10) > 5:
            self.afinado = True
        return self.afinado

    def tocar(self):
        if self.afinado:
            orquestLogs.info(f'Instrumento {self.nombre} tocando')
        else:
            raise BadTunedException(f"Instrumento {self.nombre} no afinado, no puede tocar")


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, n_cuerdas):
        super().__init__(nombre, tipo)
        self.n_cuerdas = n_cuerdas


class GuitarraElectrica(Guitarra):
    def __init__(self, nombre, tipo, n_cuerdas, potencia):
        super().__init__(nombre, tipo, n_cuerdas)
        self.potencia = potencia


class Piano(Instrumento):
    def __init__(self, nombre, tipo, n_teclas):
        super().__init__(nombre, tipo)
        self.n_teclas = n_teclas


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, size):
        super().__init__(nombre, tipo)
        self.size = size
