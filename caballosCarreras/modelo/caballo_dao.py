class CaballoDAO:
    _INSERTAR = "INSERT INTO `caballos` (`nombre`, `fecha_nacimiento`, `velocidad`, `experiencia`,\
                 `valor_apuesta`, `id_granpremio`) VALUES (%s, %s, %s, %s, %s, %s)"

    _UPDATE = "UPDATE `caballos` SET `experiencia` = %s WHERE `caballos`.`id` = %s"

    @classmethod
    def insertar(cls, caballo, cursor):
        valores = (caballo.nombre, caballo.nacimiento, caballo.velocidad, caballo.experiencia,
                   caballo.valor_apuesta, caballo.id_granpremio)
        cursor.execute(cls._INSERTAR, valores)

    @classmethod
    def update(cls, caballo, cursor):
        valores = (caballo.experiencia, caballo.idd)
        cursor.execute(cls._UPDATE, valores)
