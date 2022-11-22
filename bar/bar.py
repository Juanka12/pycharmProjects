from persona import Cliente
from persona import Camarero
import barLogs


class Bar:
    def __init__(self, nombre, camarero, cliente):
        self.nombre = nombre
        self.camarero = camarero
        self.cliente = cliente

    def iniciarJornada(self):
        taza = self.camarero.servirTaza()
        try:
            self.cliente.tomarTaza(taza)
        except Exception as e:
            barLogs.error(f'Exception - Ocurrió una excepcion: {e} , {type(e)}')


if __name__ == '__main__':
    cliente = Cliente("Juan")
    camarero = Camarero("Pepe")
    bar = Bar("San Jose", camarero, cliente)
    bar.iniciarJornada()
