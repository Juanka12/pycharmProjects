class ApostanteDAO:
    _INSERTAR = "INSERT INTO `apostantes` (`nombre`, `saldo`) VALUES (%s, %s)"

    _UPDATE = "UPDATE `apostantes` SET `saldo` = %s WHERE `apostantes`.`id` = %s"

    @classmethod
    def insertar(cls, apostante, cursor):
        valores = (apostante.nombre, apostante.saldo)
        cursor.execute(cls._INSERTAR, valores)

    @classmethod
    def update(cls, apostante, cursor):
        valores = (apostante.saldo, apostante.idd)
        cursor.execute(cls._UPDATE, valores)
