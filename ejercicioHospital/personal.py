import random
import datetime
from enfermedad import Enfermedad
from paciente import Enfermo


class Personal:
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador

    def Fichar(self):
        dt = datetime.datetime.now()
        print("El trabajador {} con identificador {} ha fichado el {}/{}/{} a las {}:{}"
              .format(self.nombre, self.identificador, dt.day, dt.month, dt.year, dt.hour, dt.minute))


class Doctor(Personal):
    def __init__(self, especialidad, nombre, identificador):
        Personal.__init__(self, nombre, identificador)
        self.especialidad = especialidad

    def Diagnosticar(self, paciente):
        # Se genera un numero del 1 al 10 y si es mayor que seis se recoge una enfermedad aleatoria para el paciente
        print("El doctor {} diagnostica al paciente {}.".format(self.nombre, paciente.nombre))
        if random.randint(1, 10) >= 7:
            enfermedad = Enfermedad.GetRandomEnfermedad()
            print("El paciente esta enfermo de {}.".format(enfermedad))
            return Enfermo(enfermedad, paciente.nombre, paciente.sintomas)
        return paciente


class Enfermero(Personal):
    def __init__(self, planta, nombre, identificador):
        Personal.__init__(self, nombre, identificador)
        self.planta = planta