from listaEnla import ListaMensajes
from nodoListaEnla import Nodo
from ClaseMensaje import Mensaje
from ClaseTorre import Torre
import datetime

class Chat:
    def __init__(self,num1,num2):
        self.numeros = (num1,num2)
        self.mensajes=ListaMensajes()
        self.fechaUltimoMensaje = datetime.datetime.now()
        
    def enviarMensaje(self, contenido, numero, torre: Torre):
        miNumero = [self.numeros[1] if self.numeros[0]==numero else self.numeros[0]]
        mensaje = Mensaje(contenido,miNumero[0], numero)
        self.mensajes.agregarFinal(Nodo(mensaje))
        print('Mensaje enviado')
        self.fechaUltimoMensaje = datetime.datetime.now()
        torre.recibirMensaje(mensaje)
    
    #def borrarMensaje(self):       #IMPORTANTE

    #def verEstadoUltimoMensaje(self):      PARA VER SI EL ULTIMO
    
    def verChat(self):
        print(self.mensajes)
    
    def __lt__(self, other):
        return self.fechaUltimoMensaje<other.fechaUltimoMensaje
    
    def __str__(self):
        return f'Chat entre {self.numeros[0]} y {self.numeros[1]}'

    def __repr__(self):
        return self.__str__()
    
    