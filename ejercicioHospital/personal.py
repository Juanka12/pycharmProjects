import random
from enfermedad import Enfermedad
from paciente import Enfermo

class Personal:
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador

    def Fichar(self):
        print("El trabajador {} con identificador {} ha fichado.".format(self.nombre, self.identificador))


class Doctor(Personal):
    def __init__(self, especialidad, nombre, identificador):
        Personal.__init__(self, nombre, identificador)
        self.especialidad = especialidad

    def Diagnosticar(self, paciente):
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