from tazaCafe import TazaCafe
import temperatureException
import random


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Cliente(Persona):
    def __init__(self, nombre):
        Persona.__init__(self, nombre)

    def tomarTaza(self, taza_cafe):
        if taza_cafe.temperature > 80:
            raise temperatureException.TooHotTemperatureException("Demasiado Caliente")
        elif taza_cafe.temperature < 20:
            raise temperatureException.TooColdTemperatureException("Demasiado Frio")


class Camarero(Persona):
    def __init__(self, nombre):
        Persona.__init__(self, nombre)

    def servirTaza(self):
        return TazaCafe(random.randint(0, 100), "Con leche")
