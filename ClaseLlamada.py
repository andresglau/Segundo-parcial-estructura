import datetime
class Llamada:
    def __init__(self, numEmisor: int, numReceptor: int):
        self.numEmisor = numEmisor
        self.numReceptor = numReceptor
        self.empezoLlamada = datetime.datetime.now()
        self.duracion = None
        
    def cortarLlamada(self):
        '''
        Corta la llamada.
        Registra la duracion de la llamada
        '''
        self.duracion = datetime.datetime.now() - self.empezoLlamada
        print(f'Se termino la llamada de duracion {self.duracion}')
        
    def __str__(self):
        return f'Llamada de {self.numEmisor} a {self.numReceptor} de {self.duracion}'   #asi le aparece a la torre. por ahora en los telefonos tambien (modificar para el final)
    def __repr__(self):
        return self.__str__()