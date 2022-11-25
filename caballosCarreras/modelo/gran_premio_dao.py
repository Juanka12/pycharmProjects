class GranPremioDAO:
    _INSERTAR = "INSERT INTO `gran_premio` (`nombre`, `distancia`, `num_carreras`) VALUES (%s, %s, %s)"

    @classmethod
    def insertar(cls, gran_premio, cursor):
        valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
        cursor.execute(cls._INSERTAR, valores)
