from collections import deque
from ClaseTorre import Torre        
from ClaseContacto import Contacto
from ClaseLlamada import Llamada

class Aplicacion:
    def __init__(self):
        pass

class AplicacionComunicacion(Aplicacion):       #ACA SE INCLUYE A TELEFONO, CONTACTOS (hay que ver SMS pero me parece que no)
    def __init__(self):
        super().__init__()
        self.contactos = {}

class Contactos(AplicacionComunicacion):
    nombre = 'Contactos'
    icono = None
    def __init__(self):
        super().__init__()
        
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
        else:
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

    #DEF VER CONTACTOS
    # def busco_contactos(self, nombre, numTelefono = None):
    #     if nombre and numTelefono:
    #         return list(filter(lambda x: (nombre, numTelefono) in x, self.contactos))
    #     return list(filter(lambda x: (nombre, None) in x, self.contactos))

class Telefono(AplicacionComunicacion):             #CREAR CLASE LLAMAD
    nombre='Telefono'
    icono=None
    
    def __init__(self,numero):
        super().__init__()
        self.miNumero = numero
        self.registroDeLlamadas = deque() #cola. ordenada de anterior a reciente
        self.enLlamada = False #y se cambia cuando esta en llamada
    
    #llamar por teclado       
    def llamar(self,numero,torre):
        if isinstance(torre,Torre): #pregunta a la torre si está disponible. si esta prendido y no está en otra llamada
            if torre.verificarEstado(self.nombre,self.miNumero) and torre.verificarEstado(self.nombre,numero): #verifico ambos numeros
                self.enLlamada = Llamada(self.miNumero, numero)
                torre.telefonosRegistrados[self.enLlamada.numReceptor].aplicaciones['Telefono'].recibirLlamada(self.enLlamada, torre)

    #recibir llamada
    def recibirLlamada(self,llamada: Llamada,torre):       
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
            torre.telefonosRegistrados[llamada.numReceptor].aplicaciones['Telefono'].recibirCorte(llamada)
            self.registrarLlamadaTorre(llamada, torre)
            
    def recibirCorte(self,llamada: Llamada):
        self.enLlamada=False
        self.registrarLlamadaTelefono(llamada)




        



