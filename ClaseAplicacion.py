from collections import deque
from ClaseTorre import Torre        
from ClaseContacto import Contacto
from ClaseLlamada import Llamada
from ClaseChat import Chat

class Aplicacion:
    def __init__(self):
        pass

class AplicacionComunicacion(Aplicacion):       #ACA SE INCLUYE A TELEFONO, CONTACTOS (hay que ver SMS pero me parece que no)
    def __init__(self, numero: int):
        self.contactos = {}
        self.miNumero = numero
    def verListaContactos(self):
        print('Lista de contactos:')
        entro=False
        for indice,nombre in enumerate(list(sorted(self.contactos))):
            if indice==0:
                entro=True
            print(self.contactos[nombre])
        if not entro:
            print('No hay contactos')
            
    def verContactosEnParticular(self, subcadena):
        contactosAMostrar=[]
        for nombreAgendado in self.contactos:
            if subcadena in nombreAgendado:
                contactosAMostrar.append(self.contactos[subcadena])
        if contactosAMostrar:
            for contacto in list(sorted(contactosAMostrar)):
                print(contacto)
        else:
            print('No hay contactos que contengan esa cadena')

class Contactos(AplicacionComunicacion):
    nombre = 'Contactos'
    icono = None
    def __init__(self, numero):
        super().__init__(numero)
        
    def agregarContacto(self, nombre, numTelefono):
        if nombre in self.contactos:
            print('Este nombre ya existe')
        elif numTelefono in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
            print('Ese numero ya existe')
        else:
            self.contactos[nombre]=Contacto(nombre,numTelefono)
    
    #si no vas a querer cambiar ambas cosas, pasar None en el parametro indicado.
    def actualizarContacto(self, nombreOriginal, nombreNuevo, numTelefonoNuevo):
        if nombreOriginal not in self.contactos:
            raise ValueError('Ese nombre no esta en tus contactos')
        elif nombreNuevo==None and numTelefonoNuevo==None:
            raise ValueError('No esta realizando ninguna modificacion')
        if nombreNuevo and numTelefonoNuevo:
            self.contactos[nombreOriginal].cambiarNombre(nombreNuevo)
            self.contactos[nombreOriginal].cambiarNumTelefono(numTelefonoNuevo)
            self.contactos[nombreNuevo]=self.contactos[nombreOriginal]
            self.contactos.pop(nombreOriginal)
        elif nombreNuevo:
            self.contactos[nombreOriginal].cambiarNombre(nombreNuevo)
            self.contactos[nombreNuevo]=self.contactos[nombreOriginal]
            self.contactos.pop(nombreOriginal)
        elif numTelefonoNuevo:
            self.contactos[nombreOriginal].cambiarNumTelefono(numTelefonoNuevo)
                
    def eliminarContacto(self,nombre):
        if nombre not in self.contactos:
            raise ValueError('Ese nombre no esta en tus contactos')
        else:
            self.contactos.pop(nombre)
            print(nombre,'eliminado')


class Telefono(AplicacionComunicacion):
    nombre='Telefono'
    icono=None
    
    def __init__(self,numero):
        super().__init__(numero)
        self.registroDeLlamadas = deque() #cola. ordenada de anterior a reciente. append, popleft
        self.enLlamada = False #y se cambia cuando esta en llamada a la Llamada correspondiente
    
    #llamar por teclado       
    def llamarPorTeclado(self,numero,torre):
        if isinstance(torre,Torre): #pregunta a la torre si está disponible. si esta prendido y no está en otra llamada
            if torre.verificarEstado(self.nombre,self.miNumero) and torre.verificarEstado(self.nombre,numero): #verifico ambos numeros
                self.enLlamada = Llamada(self.miNumero, numero)
                torre.telefonosRegistrados[self.enLlamada.numReceptor].aplicaciones['Telefono'].recibirLlamada(self.enLlamada, torre)

    #llamar a un contacto
    def llamarContacto(self, nombre, torre):
        if nombre not in self.contactos:
            raise ValueError('Ese nombre no esta en tus contactos')
        else:
            if isinstance(torre,Torre):
                if torre.verificarEstado(self.nombre,self.miNumero) and torre.verificarEstado(self.nombre, self.contactos[nombre].numTelefono):
                    self.enLlamada = Llamada(self.miNumero, self.contactos[nombre].numTelefono)
                    torre.telefonosRegistrados[self.enLlamada.numReceptor].aplicaciones['Telefono'].recibirLlamada(self.enLlamada, torre)

    #recibir llamada
    def recibirLlamada(self,llamada: Llamada,torre: Torre):       
        if llamada.numEmisor in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
            for nombre in self.contactos:                       #REEVER
                if self.contactos[nombre].numTelefono==llamada.numEmisor:
                    print('Llamada de', nombre)
        else:
            print('Llamada de', llamada.numEmisor)
        respuesta=input('Ingrese 0 para cortar, cualquier otro caracter para aceptar: ')
        # if datetime.datetime.now()-llamada.empezoLlamada > 10:
        #     aceptar = 0
        if respuesta=='0':
            torre.telefonosRegistrados[llamada.numEmisor].aplicaciones['Telefono'].enLlamada=False      #COMO SIGUE LA DURACION DE LA LLAMADA
        else:
            self.enLlamada=llamada
            
    #registrar llamada en el telefono
    def registrarLlamadaTelefono(self,llamada: Llamada):
        self.registroDeLlamadas.append(llamada)
    
    #registrar llamada en la torre
    def registrarLlamadaTorre(self,llamada: Llamada, torre: Torre):
        torre.registroDeLlamadas.append(llamada)

    #cortar llamada
    def cortarLlamada(self,torre: Torre):
        if self.enLlamada == False:
            raise ValueError('No estas en ninguna llamada')
        else:
            llamada=self.enLlamada
            llamada.cortarLlamada()
            self.enLlamada=False
            self.registrarLlamadaTelefono(llamada)
            if self.miNumero == llamada.numEmisor:
                torre.telefonosRegistrados[llamada.numReceptor].aplicaciones['Telefono'].recibirCorte(llamada)
            else:
                torre.telefonosRegistrados[llamada.numEmisor].aplicaciones['Telefono'].recibirCorte(llamada)
            self.registrarLlamadaTorre(llamada, torre)
            
    def recibirCorte(self,llamada: Llamada):
        self.enLlamada=False
        self.registrarLlamadaTelefono(llamada)
    
    def verHistorialLlamadas(self):
        for llamada in self.registroDeLlamadas:
            print(llamada)
        
class SMS(AplicacionComunicacion):
    nombre='SMS'
    icono=None

    def __init__(self, numero):
        super().__init__(numero)
        self.misChats={}        #{numero: objeto Chat}      #VER SI NUMERO ES INT O STR
        self.chatAbierto = False
    
    def crearChat(self, numero, torre:Torre):
        if not numero in torre.telefonosRegistrados or not self.miNumero in torre.telefonosRegistrados:
            raise ValueError('Hay un telefono no registrado en la central')
        elif numero in self.misChats:
            raise ValueError('Ese chat ya existe')
        self.misChats[numero]=Chat(self.miNumero,numero)
        torre.telefonosRegistrados[numero].aplicaciones['SMS'].misChats[self.miNumero]=self.misChats[numero]

    def abrirChatPorNumero(self, numero):
        if numero not in self.misChats:
            print('No existe ese chat')
        else:
            self.chatAbierto = self.misChats[numero]
        
    def abrirChatPorNombre(self, nombre):
        if nombre not in self.contactos:
            raise ValueError('Ese nombre no esta en tus contactos')
        else:
            if self.contactos[nombre].numTelefono not in self.misChats:
                print('No existe ese chat')
            else:
                self.chatAbierto = self.misChats[self.contactos[nombre].numTelefono]
    
    def cerrarChat(self):
       self.chatAbierto = False
    
    def verChats(self):
        for chat in list(sorted(self.misChats.values(), reverse = True)):
            print(chat)
            
    def borrarChat(self, numero, torre: Torre):
        if numero not in self.misChats:
            print('No existe ese chat')
        else:
            self.misChats.pop(numero)
            torre.telefonosRegistrados[numero].aplicaciones['SMS'].misChats.pop(self.miNumero) #Aunque no suceda en la realidad, si alguien borra un chat, se elimina para ambos
