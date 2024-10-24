import datetime
class Llamada:
    def __init__(self, numEmisor, numReceptor):
        self.numEmisor = numEmisor
        self.numReceptor = numReceptor
        self.empezoLlamada = datetime.datetime.now()
        self.terminoLlamada = None
        self.duracion = None
    def cortarLlamada(self):
        self.terminoLlamada = datetime.datetime.now()
        self.duracion = self.terminoLlamada - self.empezoLlamada
    def __str__(self):
        #perfeccionar que es lo que muestra
        return f'Llamada de {self.numEmisor} a {self.numReceptor} de {self.duracion}'   #asi le aparece a la torre. por ahora en los telefonos tambien
    def __repr__(self):
        return self.__str__()