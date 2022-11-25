class Apostante:
    def __init__(self, idd, nombre, saldo):
        self._idd = idd
        self._nombre = nombre
        self._saldo = saldo
        self._saldo_apostado = 0
        self._caballo_apostado = ""

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
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def saldo_apostado(self):
        return self._saldo_apostado

    @saldo_apostado.setter
    def saldo_apostado(self, saldo_apostado):
        self._saldo_apostado = saldo_apostado

    @property
    def caballo_apostado(self):
        return self._caballo_apostado

    @caballo_apostado.setter
    def caballo_apostado(self, caballo_apostado):
        self._caballo_apostado = caballo_apostado

    def incrementar_saldo(self, valor_apuesta):
        incremento = self.saldo_apostado * valor_apuesta
        self.saldo += incremento
        return incremento
