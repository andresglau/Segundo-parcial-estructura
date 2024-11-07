import datetime
class Nota:
    def __init__(self,titulo,contenido):
        self.titulo=titulo
        self.contenido=contenido
        self.ultimaModificacion=datetime.datetime.now()
        
    def escribirNota(self):
        self.contenido=input("Escriba la nota... ")
        self.ultimaModificacion=datetime.datetime.now()
        
    def agregarContenido(self):
        self.contenido+=input('Agregue a su nota... ')
        self.ultimaModificacion=datetime.datetime.now()
        
    def verNota(self):
        print(self.contenido)
        
    def __lt__(self, other):
        return self.ultimaModificacion < other.ultimaModificacion   


    def __repr__(self):
        return self.__str__()
        
    