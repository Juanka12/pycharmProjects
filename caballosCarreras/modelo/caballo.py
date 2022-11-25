import random
from _datetime import datetime

class Caballo:
    def __init__(self, idd, nombre, nacimiento, velocidad, experiencia, valor_apuesta, id_granpremio):
        self._idd = idd
        self._nombre = nombre
        self._nacimiento = nacimiento
        self._velocidad = velocidad
        self._experiencia = experiencia
        self._valor_apuesta = valor_apuesta
        self._id_granpremio = id_granpremio
        self._dist_recorrida = 0

    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self, idd):
        self._idd = idd

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nacimiento(self):
        return self._nacimiento

    @nacimiento.setter
    def nacimiento(self, nacimiento):
        self._nacimiento = nacimiento

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    @property
    def valor_apuesta(self):
        return self._valor_apuesta

    @valor_apuesta.setter
    def valor_apuesta(self, valor_apuesta):
        self._valor_apuesta = valor_apuesta

    @property
    def id_granpremio(self):
        return self._id_granpremio

    @id_granpremio.setter
    def id_granpremio(self, id_granpremio):
        self._id_granpremio = id_granpremio

    @property
    def dist_recorrida(self):
        return self._dist_recorrida

    @dist_recorrida.setter
    def dist_recorrida(self, dist_recorrida):
        self._dist_recorrida = dist_recorrida

    def __str__(self):
        return self.nombre + " " + str(self.nacimiento)+" "+str(self.id_granpremio)

    def calcular_avance(self):
        edad = datetime.strptime(self.nacimiento, '%Y-%m-%d').date()
        return self.velocidad+self.experiencia-int(datetime.now().year-edad.year)+random.randint(1,50)
