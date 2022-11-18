# Press the green button in the gutter to run the script.
from hospital import Hospital
from paciente import Paciente
from personal import Doctor, Enfermero

if __name__ == '__main__':
    doctor1 = Doctor("Cardiologo", "Antonio", "001")
    doctor2 = Doctor("Neurologo", "Paco", "002")
    enfermero1 = Enfermero("1", "Pedro", "003")
    enfermero2 = Enfermero("2", "Alfonso", "004")
    personal = [doctor1, doctor2, enfermero1, enfermero2]

    paciente1 = Paciente("Alex", "Tos")
    paciente2 = Paciente("Ana", "Dolor de cabeza")
    paciente3 = Paciente("Andrea", "Hinchazon")
    paciente4 = Paciente("Carlos", "Mareo")
    pacientes = [paciente1, paciente2, paciente3, paciente4]

    hospital = Hospital("San Juan", personal, pacientes)
    hospital.IniciarJornada()
