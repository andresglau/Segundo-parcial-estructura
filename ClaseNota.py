import datetime

class Nota:
    def __init__(self,titulo,contenido):
        self.titulo=titulo
        self.contenido=contenido
        self.ultimaModificacion=datetime.datetime.now()
        
    def sobreescribirNota(self):
        '''
        Reescribe la nota desde 0
        '''
        self.contenido=input("Escriba el contenido: ")
        self.ultimaModificacion=datetime.datetime.now()
        
    def agregarContenido(self):
        '''
        Agrega el contenido a la nota
        '''
        self.contenido+=input('Agregue a su nota... ')
        self.ultimaModificacion=datetime.datetime.now()
        
    def verNota(self):
        print(f'Titulo: {self.titulo}\n{self.contenido}')
        
    def __lt__(self, other):
        return self.ultimaModificacion < other.ultimaModificacion   

    def __str__(self):
        return f'Nota con titulo: {self.titulo}'

    def __repr__(self):
        return self.__str__()