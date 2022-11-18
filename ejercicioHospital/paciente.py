class Paciente:
    def __init__(self, nombre, sintomas):
        self.nombre = nombre
        self.sintomas = sintomas


class Enfermo(Paciente):
    def __init__(self, enfermedad, nombre, sintomas):
        Paciente.__init__(self, nombre, sintomas)
        self.enfermedad = enfermedad