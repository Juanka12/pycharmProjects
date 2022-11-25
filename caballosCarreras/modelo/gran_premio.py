class GranPremio:
    def __init__(self, idd, nombre, distancia, num_carreras):
        self._idd = idd
        self._nombre = nombre
        self._distancia = distancia
        self._num_carreras = num_carreras

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
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, distancia):
        self._distancia = distancia

    @property
    def num_carreras(self):
        return self._num_carreras

    @num_carreras.setter
    def num_carreras(self, num_carreras):
        self._num_carreras = num_carreras
