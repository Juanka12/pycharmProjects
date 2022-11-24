import utils.customLogs as logs


class IOHandler:
    def __init__(self, nombre, mode):
        self.nombre = nombre
        self.mode = mode

    def __enter__(self):
        logs.info(f'Abriendo archivo {self.nombre}')
        self.nombre = open(self.nombre, self.mode, encoding='utf-8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        logs.info(f'Cerrando el archivo {self.nombre.name}')
        if self.nombre:
            self.nombre.close()