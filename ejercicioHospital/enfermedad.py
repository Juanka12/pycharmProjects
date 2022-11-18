from enum import Enum
import random


class Enfermedad(Enum):
    Covid = 1
    Bronquitis = 2
    Resfriado = 3
    Varicela = 4
    Alergia = 5

    def GetRandomEnfermedad():
        return Enfermedad(random.randint(0, 5)).name
