import colegioLogs


class IOHandler:
    def __init__(self, nombre, mode):
        self.nombre = nombre
        self.mode = mode

    def __enter__(self):
        colegioLogs.info(f'Abriendo archivo {self.nombre}')
        self.nombre = open(self.nombre, self.mode, encoding='utf-8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        colegioLogs.info(f'Cerrando el archivo {self.nombre.name}')
        if self.nombre:
            self.nombre.close()