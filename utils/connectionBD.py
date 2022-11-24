import sys
import MySQLdb
import psycopg2
import utils.configBD as configBD


def get_mysql_conection():
    return get_conection()


def get_conection(db=configBD.db, maquina=configBD.maquina, usuario=configBD.usuario, password=configBD.password,
                  base_datos=configBD.base_datos, puerto=configBD.puerto):
    try:
        if db == "mysql":
            conection = MySQLdb.connect(
                host=maquina,
                user=usuario,
                passwd=password,
                db=base_datos,
                port=puerto)
        else:
            conection = psycopg2.connect(
                user=usuario,
                password=password,
                host=maquina,
                port=puerto,
                database=base_datos
            )
    except MySQLdb.Error as mysqle:
        print("No puedo conectar a la base de datos:", mysqle)

    except Exception as e:
        print("No puedo conectar a la base de datos:", e)

    else:
        print("Conexión correcta.")

    return conection