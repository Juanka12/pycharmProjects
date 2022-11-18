from paciente import Enfermo
from personal import Doctor


class Consulta:
    def __init__(self, doctor):
        self.doctor = doctor

    def PasarConsulta(self, paciente):
        # Una vez en consulta, el doctor diagnostica al paciente, si es de tipo enfermo pasa a una habitacion
        print("El paciente {} pasa a consulta.".format(paciente.nombre))
        npaciente = self.doctor.Diagnosticar(paciente)
        if type(npaciente) is Enfermo:
            print("El paciente {} pasara a una habitacion.".format(npaciente.nombre))
        else:
            print("El paciente {} no estaba enfermo, para casa.".format(paciente.nombre))


class Hospital:
    def __init__(self, nombre, personal, sala_espera):
        self.personal = personal
        self.consultas = []
        self.sala_espera = sala_espera
        self.doctores = []
        self.enfermeros = []
        self.SepararPersonal()

    def SepararPersonal(self):
        # Separa la lista personal en dos listas doctores y enfermeros
        for persona in self.personal:
            if type(persona) is Doctor:
                self.doctores.append(persona)
                self.consultas.append(Consulta(persona))
            else:
                self.enfermeros.append(persona)

    def IniciarJornada(self):
        # Ordena al personal a fichar
        print("Iniciando jornada.")
        for persona in self.personal:
            persona.Fichar()
        self.AtenderPacientes()

    def AtenderPacientes(self):
        # Recoge los pacientes de la lista sala_espera y entran a cada consulta diferente
        while len(self.sala_espera) > 0:
            for i, persona in enumerate(self.enfermeros):
                paciente = self.sala_espera.pop(0)
                print()
                print("Enfermero {} lleva a paciente {} a la consulta {}.".format(persona.nombre, paciente.nombre, i + 1))
                self.consultas[i].PasarConsulta(paciente)