import orquestLogs
import instrumento
from badTunedException import BadTunedException


class Orquesta:
    def __init__(self):
        self.instrumentos = []

    def crear_orquesta(self, instrumentos):
        self.instrumentos = instrumentos

    def iniciar_concierto(self):
        for instrument in self.instrumentos:
            instrument.afinar()
        for instrument in self.instrumentos:
            try:
                instrument.tocar()
            except BadTunedException as e:
                orquestLogs.error(f'Exception - Ocurrió una excepcion: {e}')
            except Exception as e:
                orquestLogs.error(f'Exception - Ocurrió una excepcion: {e} , {type(e)}')


if __name__ == "__main__":
    orquesta = Orquesta()
    guitarra = instrumento.Guitarra("guitarra", "cuerda", "5")
    guitarra_electrica = instrumento.GuitarraElectrica("guitarra_electrica", "cuerda", "5", "200W")
    piano = instrumento.Piano("piano", "cuerda", "36")
    tambor = instrumento.Tambor("tambor", "percusion", "30cm")
    orquesta.crear_orquesta([guitarra, piano, guitarra_electrica, tambor])
    orquesta.iniciar_concierto()
