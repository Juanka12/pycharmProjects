class TemperatureException(Exception):

    def __init__(self, message):
        self.message = message


class TooHotTemperatureException(TemperatureException):
    def __init__(self, message):
        self.message = message


class TooColdTemperatureException(TemperatureException):
    def __init__(self, message):
        self.message = message
        