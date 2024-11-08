from collections import deque
from ClaseContacto import Contacto
# from ClaseContacto import Contacto
# from datetime import datetime
# from ClaseChat import *

data = {'Pedro': Contacto('Pedro', 1122435566), 'Andi': Contacto('Andi', 1122334455)}
next((item.numTelefono for item in data if item.numTelefono == 1122435566), None)

class Contacto:
    def __init__(self, nombre, numTelefono = None):
        self.nombre = nombre
        self.numTelefono = numTelefono

class Aplicacion():
    aplicacionesDisponibles={}
    nombre = ''
    icono = None
    def __init__(self):
        pass

class AplicacionComunicacion(Aplicacion):       #ACA SE INCLUYE A TELEFONO, CONTACTOS (hay que ver SMS pero me parece que no)
    def __init__(self):
        super().__init__()
        self.contactos = {}
    #agregar contacto. no hace falta verificar que exista ya que es lo que uno tiene agendado       #NO HAY REPETIDOS, ACLARAR
    def agregarContacto(self, nombre, numTelefono = None):
        self.contactos.update({(nombre, numTelefono): Contacto(nombre, numTelefono)})
    def actualizarContacto(self, nombre, numTelefono = None, nuevoNom = None, nuevoNum = None):
        if not (nuevoNom or nuevoNum):
            print('Debe pasar un atributo para poder modificar el contacto')
        # self.contactos.update({nombre, None}: )
    
    def busco_contactos(self, nombre, numTelefono = None):
        if nombre and numTelefono:
            return list(filter(lambda x: (nombre, numTelefono) in x, self.contactos))
        return list(filter(lambda x: (nombre, None) in x, self.contactos))

    #         self.contactos.update
            
    #eliminar contacto
    # def eliminarContacto(self, nombre):
    #     if nombre not in self.contactos:
    #         raise ValueError('No existe este contacto')
    #     else:
    #         self.contactos.pop(nombre)
    def verContactos(self):
        for elem in self.contactos:
            nom = elem.items()
            print(f'{nom} // ')
        
app = AplicacionComunicacion()
app.agregarContacto('Isidro', 1234567)
app.agregarContacto('Isidro', 1234567)
print(app.contactos)
# app.verContactos()

class Telefono(AplicacionComunicacion):
    nombre = 'Telefono'
    icono = None        #DEFINIR
    def __init__(self, miNumero):
        super().__init__()
        self.miNumero = miNumero
        self.registroLlamadas = deque()     #cola. FIFO. appendleft

#################################################################################################

    
    #actualizar contacto        
    def actualizarContacto(self, nombre, numero):
        if nombre not in self.contactos:
            raise ValueError('No existe este contacto')
        else:
            self.contactos[nombre]=numero
    
    #verContactos
    def verContactos(self):
        for nombre in list(sorted(self.contactos.keys())):
            print(nombre, end=' ')
        
        
        
        
# class SMS(Aplicacion):
#     def __init__(self):
#         self.contactosMensajes={}
#         self.casillaMensajes=deque()
import time
# from ClaseChat import Chat

# a=Chat(4,5)
# time.sleep(2)
# b=Chat(5,6)
# time.sleep(5)
# c=Chat(5,7)

# dic={4:a,6:b,7:c}

# b.enviarMensaje('hola',6)

# for chat in list(sorted(dic.values(), reverse = True)):
#     print(chat)

# class Mensaje:
#     def __init__(self, con):
#         self.con = con
# a= deque()
# a.append(Mensaje('rr'))
# print('Antes')
# print(type(a))
# print(a)
# a.clear()
# print('Despues')
# print(a)
# print(type(a))

print(type(1234)==int)