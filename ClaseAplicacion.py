from collections import deque
from ClaseTorre import Torre        
from ClaseContacto import Contacto
from ClaseLlamada import Llamada
from ClaseChat import Chat
import Validaciones

class Aplicacion:
    def __init__(self):
        self.opciones = None
    
    def volver(self):
        return True

class AplicacionComunicacion(Aplicacion):
    def __init__(self, numero: int, torre: Torre):
        super().__init__()
        self.contactos = {}     #La lista de contactos 
        self.miNumero = numero
        self.torre=torre
    
    def verListaContactos(self):
        '''
        Imprime la lista de contactos del celular
        '''
        print('Lista de contactos:')
        if self.contactos:
            for nombre in list(sorted(self.contactos)):
                print(self.contactos[nombre])
        else:
            print('No hay contactos')
            
    def verContactosEnParticular(self):
        subcadena=input('Ingrese una subcadena para filtrar contactos: ')
        contactosAMostrar=[]
        for nombreAgendado in self.contactos:
            if subcadena in nombreAgendado:
                contactosAMostrar.append(self.contactos[nombreAgendado])
        if contactosAMostrar:
            for contacto in list(sorted(contactosAMostrar)):
                print(contacto)
        else:
            print('No hay contactos que contengan esa cadena')

class Contactos(AplicacionComunicacion):
    nombre = 'Contactos'
    icono = None
    def __init__(self, numero, torre: Torre):
        super().__init__(numero, torre)
        self.opciones = [('Ver contactos',self.verListaContactos,[]),
                         ('Ver contactos en particular',self.verContactosEnParticular,[]),
                         ('Agregar contacto', self.agregarContacto,[]),
                         ('Actualizar contacto',self.actualizarContacto,[]),
                         ('Eliminar contacto',self.eliminarContacto,[]),
                         ('Volver a pantalla de inicio', self.volver, [])]

    def agregarContacto(self):
        ''
        nombre = input('Ingrese el nombre para agendar el contacto: ')
        if nombre in self.contactos:
            print('Este nombre ya existe')
        else:
            numTelefono = input('Ingrese un numero de telefono para el contacto: ')
            if Validaciones.validarFormatoNumTelefono(numTelefono):
                pass
            elif numTelefono in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
                print('Ese numero ya esta agendado')
            else:
                self.contactos[nombre]=Contacto(nombre,numTelefono)
    
    #si no vas a querer cambiar ambas cosas, pasar None en el parametro indicado.
    def actualizarContacto(self):
        try:
            nombreOriginal=input('Ingrese el nombre del contacto a modificar: ')
            if nombreOriginal not in self.contactos:
                raise ValueError('Ese nombre no esta en tus contactos')
            nombreNuevo=input('Ingrese el nombre nuevo. Si solo desea cambiar el numero, toque enter: ')
            numTelefonoNuevo=input('Ingrese el numero nuevo. Si solo desea cambiar el nombre, toque enter: ')
            if nombreNuevo=='' and numTelefonoNuevo=='':
                raise ValueError('No esta realizando ninguna modificacion')
            if nombreNuevo and numTelefonoNuevo:
                if Validaciones.validarFormatoNumTelefono(numTelefonoNuevo):
                    pass
                elif numTelefonoNuevo in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
                    print('Ese numero ya esta agendado')
                else:
                    self.contactos[nombreOriginal].cambiarNombre(nombreNuevo)
                    self.contactos[nombreOriginal].cambiarNumTelefono(numTelefonoNuevo)
                    self.contactos[nombreNuevo]=self.contactos[nombreOriginal]
                    self.contactos.pop(nombreOriginal)
            elif nombreNuevo:
                self.contactos[nombreOriginal].cambiarNombre(nombreNuevo)
                self.contactos[nombreNuevo]=self.contactos[nombreOriginal]
                self.contactos.pop(nombreOriginal)
            elif numTelefonoNuevo:
                if Validaciones.validarFormatoNumTelefono(numTelefonoNuevo):
                    pass
                elif numTelefonoNuevo in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
                    print('Ese numero ya esta agendado')
                else:
                    self.contactos[nombreOriginal].cambiarNumTelefono(numTelefonoNuevo)
        except ValueError as e:
            print(e)
                
    def eliminarContacto(self):
        try:
            nombre=input('Ingrese el nombre del contacto a eliminar: ')
            if nombre not in self.contactos:
                raise ValueError('Ese nombre no esta en tus contactos')
            else:
                self.contactos.pop(nombre)
                print(nombre,'eliminado')
        except ValueError as e:
            print(e)
        

class Telefono(AplicacionComunicacion):
    nombre='Telefono'
    icono=None
    
    def __init__(self,numero, torre: Torre):
        super().__init__(numero, torre)
        self.registroDeLlamadas = deque() #cola. ordenada de anterior a reciente. append, popleft
        self.enLlamada = False #y se cambia cuando esta en llamada a la Llamada correspondiente
        self.opciones = [('Ver contactos',self.verListaContactos,[]),
                         ('Ver contactos en particular',self.verContactosEnParticular,[]),
                         ('Llamar por teclado', self.llamarPorTeclado, []),
                         ('Llamar por contacto', self.llamarContacto, []),
                         ('Cortar llamada',self.cortarLlamada,[]),
                         ('Ver historial llamadas', self.verHistorialLlamadas,[]),
                         ('Volver a pantalla de inicio', self.volver, [])]
    
    #llamar por teclado       
    def llamarPorTeclado(self):
        '''
        Llama a un numero de telefono mediante el teclado de la aplicacion
        Si intenta llamar al propio celular, levanta un error
        '''
        numero = input('Ingrese el numero al que desea llamar: ')
        if Validaciones.validarFormatoNumTelefono(numero):
            print('Intento llamar a un numero de telefono invalido')
        else:
            numero=int(numero)
            try:
                if numero==self.miNumero:
                    raise ValueError('No te podes llamar a vos mismo')
            except ValueError as e:
                print(e)
            else:
                if self.torre.verificarEstado(self.nombre,self.miNumero) and self.torre.verificarEstado(self.nombre,numero): #verifico ambos numeros
                    self.enLlamada = Llamada(self.miNumero, numero)
                    self.torre.telefonosRegistrados[self.enLlamada.numReceptor].aplicaciones['Telefono'].recibirLlamada(self.enLlamada)


    #llamar a un contacto
    def llamarContacto(self):
        try:
            nombre = input('Ingrese el nombre del contacto que desea llamar: ')
            if nombre not in self.contactos:
                raise ValueError('Ese nombre no esta en tus contactos')
        except ValueError as e:
            print(e)
        else:
            if self.torre.verificarEstado(self.nombre,self.miNumero) and self.torre.verificarEstado(self.nombre, self.contactos[nombre].numTelefono):
                    self.enLlamada = Llamada(self.miNumero, self.contactos[nombre].numTelefono)
                    self.torre.telefonosRegistrados[self.enLlamada.numReceptor].aplicaciones['Telefono'].recibirLlamada(self.enLlamada)


    #recibir llamada
    def recibirLlamada(self,llamada: Llamada):
        print(f'\n(Se esta operando el telefono: {llamada.numReceptor})')       
        if llamada.numEmisor in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
            for nombre in self.contactos:                       #REEVER
                if self.contactos[nombre].numTelefono==llamada.numEmisor:
                    print('Llamada de', nombre)
        else:
            print('Llamada entrante de', llamada.numEmisor)
        respuesta=input('Ingrese 0 para cortar, cualquier otro caracter para aceptar: ')
        # if datetime.datetime.now()-llamada.empezoLlamada > 10:
        #     aceptar = 0
        if respuesta=='0':
            self.torre.telefonosRegistrados[llamada.numEmisor].aplicaciones['Telefono'].enLlamada=False #COMO SIGUE LA DURACION DE LA LLAMADA
            print('Llamada rechazada')
        else:
            self.enLlamada=llamada
            print('Llamada en curso')
            
    #registrar llamada en el telefono
    def registrarLlamadaTelefono(self,llamada: Llamada):
        self.registroDeLlamadas.append(llamada)
    
    #registrar llamada en la torre
    def registrarLlamadaTorre(self,llamada: Llamada):
        self.torre.registroDeLlamadas.append(llamada)

    #cortar llamada
    def cortarLlamada(self):
        try:
            if self.enLlamada == False:
                raise ValueError('No estas en ninguna llamada')
        except ValueError as e:
            print(e)
        else:
                llamada=self.enLlamada
                llamada.cortarLlamada()
                self.enLlamada=False
                self.registrarLlamadaTelefono(llamada)
                if self.miNumero == llamada.numEmisor:
                    self.torre.telefonosRegistrados[llamada.numReceptor].aplicaciones['Telefono'].recibirCorte(llamada)
                else:
                    self.torre.telefonosRegistrados[llamada.numEmisor].aplicaciones['Telefono'].recibirCorte(llamada)
                self.registrarLlamadaTorre(llamada)
            
    def recibirCorte(self,llamada: Llamada):
        self.enLlamada=False
        self.registrarLlamadaTelefono(llamada)
    
    def verHistorialLlamadas(self):
        print('Historial de llamadas:')
        for llamada in self.registroDeLlamadas:
            print(llamada)
        
class SMS(AplicacionComunicacion):
    nombre='SMS'
    icono=None
    
    def __init__(self, numero, torre: Torre):
        super().__init__(numero, torre)
        self.misChats={}                #{numero: objeto Chat}
        self.chatAbierto=False
        self.opciones = [
                        ('Ver contactos',self.verListaContactos,[]),
                         ('Ver contactos en particular',self.verContactosEnParticular,[]),
                         ('Crear un chat nuevo',self.crearChat,[]),
                         ('Abrir un chat por numero',self.abrirChatPorNumero,[]),
                         ('Abrir un chat por nombre del contacto',self.abrirChatPorNombre,[]),
                         ('Ver los chats',self.verChats,[]),
                         ('Borrar un chat',self.borrarChat,[]),
                         ('Cerrar chat',self.cerrarChat,[]),
                         ('Enviar un mensaje al chat abierto',self.enviarMensaje,[]),
                         ('Borrar un mensaje del chat abierto', self.borrarMensaje,[]),
                         ('Ver chat abierto',self.verChatAbierto,[]),
                         ('Volver a pantalla de inicio', self.volver, [])
                         ]
    
    def crearChat(self):
        numero=input('Ingrese el numero de la persona con la que desea crear el chat: ')
        if Validaciones.validarFormatoNumTelefono(numero):
            pass
        else:
            try:
                numero=int(numero)
                if not numero in self.torre.telefonosRegistrados or not self.miNumero in self.torre.telefonosRegistrados:
                    raise ValueError('Hay un telefono no registrado en la central')
                elif numero in self.misChats:
                    raise ValueError('Ese chat ya existe')
            except ValueError as e:
                print(e)
            else:
                chat=Chat(self.miNumero,numero)
                self.misChats[numero]=chat
                self.torre.telefonosRegistrados[numero].aplicaciones['SMS'].misChats[self.miNumero]=chat
                print(chat,'creado')

    def abrirChatPorNumero(self):
        if self.chatAbierto==False:
            try:
                numero = int(input('Ingrese el numero de telefono del chat que desea abrir: '))
            except ValueError:
                print('No ingreso un numero')
            else:
                if numero not in self.misChats:
                    print('No existe ese chat')
                else:
                    self.chatAbierto = self.misChats[numero]
                    print('Se abrio el chat')
        else:
            print('Ya hay un chat abierto')
        
    def abrirChatPorNombre(self):
        if self.chatAbierto==False:
            try:
                nombre = input('Ingrese el nombre del contacto del chat que desea abrir: ')
                if nombre not in self.contactos:
                    raise ValueError('Ese nombre no esta en tus contactos')
            except ValueError as e:
                print(e)
            else:
                if self.contactos[nombre].numTelefono not in self.misChats:
                    print('No existe ese chat')
                else:
                    self.chatAbierto = self.misChats[self.contactos[nombre].numTelefono]
                    print('Se abrio el chat')
        else:
            print('Ya hay un chat abierto')
                
    def cerrarChat(self):
        self.chatAbierto = False
        print('Se cerro el chat')
        
    
    def verChats(self): #ver como hacer para printear nombre/numero
        if self.misChats:
            for chat in list(sorted(self.misChats.values(), reverse = True)):
                print(chat)
        else:
            print('No hay chats')

    def borrarChat(self):
        numero=input('Ingrese el numero de la persona con la que desea borrar el chat: ')
        if Validaciones.validarFormatoNumTelefono(numero):
            pass
        else:
            numero=int(numero)
            if numero not in self.misChats:
                print('No existe ese chat')
            elif self.chatAbierto==self.misChats[numero]:
                print('No podes borrar el chat abierto')
            else:
                print(self.misChats[numero],'eliminado')
                self.misChats.pop(numero)
                self.torre.telefonosRegistrados[numero].aplicaciones['SMS'].misChats.pop(self.miNumero) #Aunque no suceda en la realidad, si alguien borra un chat, se elimina para ambos
                
    def enviarMensaje(self):
        if not self.chatAbierto:
            print('No hay ningun chat abierto')
        else:
            contenido=input('Ingrese el mensaje que desea enviar: ')
            self.chatAbierto.enviarMensaje(contenido, self.miNumero, self.torre)
    
    def verChatAbierto(self):
        if not self.chatAbierto:
            print('No hay ningun chat abierto')
        else:
            self.chatAbierto.verChat()
            
    def borrarMensaje(self):
        if not self.chatAbierto:
            print('No hay ningun chat abierto')
        else:
            self.chatAbierto.verChat()
            try:
                pos=int(input('Ingrese la posicion del mensaje que desea eliminar: '))
            except ValueError:
                print('No ingreso un numero entero')
            else:
                self.chatAbierto.borrarMensaje(pos)