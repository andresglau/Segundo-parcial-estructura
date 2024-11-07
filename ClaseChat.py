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
        
    def enviarMensaje(self, contenido, miNumero, torre: Torre):
        otroNumero = [self.numeros[1] if self.numeros[0]==miNumero else self.numeros[0]]
        mensaje = Mensaje(contenido, miNumero, otroNumero[0])
        self.mensajes.agregarFinal(Nodo(mensaje))
        print('Mensaje enviado')
        self.fechaUltimoMensaje = datetime.datetime.now()
        torre.recibirMensaje(mensaje)

    def borrarMensaje(self, pos):
        self.mensajes.eliminarMensaje(pos)
    
    def verChat(self):
        if self.mensajes.esVacia():
            print('No hay mensajes')
        else:
            print(self.mensajes)
    
    def __lt__(self, other):
        return self.fechaUltimoMensaje<other.fechaUltimoMensaje
    
    def __str__(self):
        return f'Chat entre {self.numeros[0]} y {self.numeros[1]}'

    def __repr__(self):
        return self.__str__()