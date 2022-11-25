import logging
from caballosCarreras.modelo.apostante_dao import ApostanteDAO
from caballosCarreras.modelo.gran_premio_dao import GranPremioDAO
from utils.connectionBD import get_mysql_conection
import utils.customLogs as logs
from caballosCarreras.modelo.caballo_dao import CaballoDAO


class AccessDB:

    def __init__(self):
        try:
            self.connection = get_mysql_conection()
            self.cursor = self.connection.cursor()
            logs.debug("Conexion abierta")
        except Exception as e:
            logs.error(f"Error al abrir conexion {e}")

    def close(self):
        self.cursor.close()
        self.connection.close()
        logs.debug("Conexion cerrada")

    def crear_tablas(self):
        try:
            self.cursor.execute('CREATE TABLE apostantes (id int AUTO_INCREMENT, nombre varchar(30),\
             saldo int, PRIMARY KEY (id))')

            self.cursor.execute('CREATE TABLE gran_premio (id int AUTO_INCREMENT, nombre varchar(30), distancia int,\
            num_carreras int, PRIMARY KEY (id))')

            self.cursor.execute('CREATE TABLE caballos (id int AUTO_INCREMENT, nombre varchar(30),fecha_nacimiento date,\
            velocidad int, experiencia int, valor_apuesta int, id_granpremio int, PRIMARY KEY (id))')

        except Exception as e:
            logs.error("Error", e)

    def insertar_caballos(self, caballo):
        try:
            CaballoDAO.insertar(caballo, self.cursor)
            self.connection.commit()
            logs.debug("Caballo insertado")
        except Exception as e:
            logs.error("Error", e)

    def insertar_apostantes(self, apostante):
        try:
            ApostanteDAO.insertar(apostante, self.cursor)
            self.connection.commit()
            logs.debug("Apostante insertado")
        except Exception as e:
            logs.error("Error", e)

    def insertar_grandes_premios(self, gran_premio):
        try:
            GranPremioDAO.insertar(gran_premio, self.cursor)
            self.connection.commit()
            logs.debug("Gran Premio insertado")
        except Exception as e:
            logs.error("Error", e)

    def actualizar_caballos(self, caballo):
        try:
            CaballoDAO.update(caballo, self.cursor)
            self.connection.commit()
            logging.debug("Caballo actualizado")
        except Exception as e:
            logs.error("Error", e)

    def actualizar_apostantes(self, apostante):
        try:
            ApostanteDAO.update(apostante, self.cursor)
            self.connection.commit()
            logging.debug("Apostante actualizado")
        except Exception as e:
            logs.error("Error", e)