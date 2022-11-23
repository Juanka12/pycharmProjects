class Alumno:
    def __init__(self, nombre, apellidos, dni, materias):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.materias = materias

    def __str__(self):
        return f"{self.nombre}|{self.apellidos}|{self.dni}|"+";".join(self.materias)

class Colegio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def addAlumno(self, alumno):
        self.alumnos.append(alumno)

    def __repr__(self):
        return self.nombre