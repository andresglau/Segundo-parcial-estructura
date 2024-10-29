import datetime
class Mensaje:
    def __init__(self, contenido: str, numEmisor: int, numReceptor: int):
        self.contenido = contenido
        self.numEmisor = numEmisor
        self.numReceptor = numReceptor
        self.fechaEnviado = datetime.datetime.now()
        self.entregado = False
    
    def __str__(self):
        return f'Num {self.numEmisor} ha enviado a num {self.numReceptor}: {self.contenido}\n Enviado el {self.fechaEnviado}'
        
    def __repr__(self):
        return self.__str__()