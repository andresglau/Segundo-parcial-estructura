from collections import deque
from ClaseTorre import Torre        
from ClaseContacto import Contacto
from ClaseLlamada import Llamada
from ClaseChat import Chat
import Validaciones

class Aplicacion:
    def __init__(self):
        self.opciones = [('Volver a pantalla de inicio', self.volver, [])]
    
    def volver(self):
        return True

class AplicacionComunicacion(Aplicacion):
    def __init__(self, numero: int, torre: Torre):
        super().__init__()
        self.contactos = {}    #La lista de contactos {nombre : objeto Contacto}
        self.miNumero = numero
        self.torre=torre
    
    def verListaContactos(self):
        '''
        Imprime la lista de contactos del celular ordenada alfabeticamente
        '''
        print('Lista de contactos:')
        if self.contactos:
            for nombre in list(sorted(self.contactos)):
                print(self.contactos[nombre])
        else:
            print('No hay contactos')
            
    def verContactosEnParticular(self):
        '''
        Imprime alfabeticamente los contactos que contienen la subcadena ingresada
        '''
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
    icono = 'FotosApps/FotoAppContactos.jpg'
    def __init__(self, numero, torre: Torre):
        super().__init__(numero, torre)
        self.opciones = [('Ver contactos',self.verListaContactos,[]),
                         ('Ver contactos en particular',self.verContactosEnParticular,[]),
                         ('Agregar contacto', self.agregarContacto,[]),
                         ('Actualizar contacto',self.actualizarContacto,[]),
                         ('Eliminar contacto',self.eliminarContacto,[]),
                         ('Volver a pantalla de inicio', self.volver, [])]

    def agregarContacto(self):
        '''
        Agrega un contacto en base a los datos que le pase el usuario.
        Los nombres con los que agenda los contactos son unicos
        Ademas el numero de telefono que agenda en ese contacto debe ser valido y no debe estar agendado
        '''
        nombre = input('Ingrese el nombre para agendar el contacto: ')
        if nombre in self.contactos:
            print('Este nombre ya existe')
        else:
            numTelefono = input('Ingrese un numero de telefono para el contacto: ')
            if Validaciones.validarFormatoNumTelefono(numTelefono):
                pass
            else:
                numTelefono=int(numTelefono)
                if numTelefono in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
                    print('Ese numero ya esta agendado')
                else:
                    self.contactos[nombre]=Contacto(nombre,numTelefono)
    
    def actualizarContacto(self):
        '''
        Pide los datos a cambiar de un contacto.
        Puede cambiar nombre, numero de telefono o los dos
        Si no cambia ninguno o intenta cambiar un contacto que no esta agendado, lanza un error
        '''
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
                else:
                    numTelefonoNuevo=int(numTelefonoNuevo)
                    if numTelefonoNuevo in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
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
            else:
                if Validaciones.validarFormatoNumTelefono(numTelefonoNuevo):
                    pass
                else:
                    numTelefonoNuevo=int(numTelefonoNuevo)
                    if numTelefonoNuevo in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
                        print('Ese numero ya esta agendado')
                    else:
                        self.contactos[nombreOriginal].cambiarNumTelefono(numTelefonoNuevo)
        except ValueError as e:
            print(e)
                
    def eliminarContacto(self):
        '''
        Elimina un contacto.
        '''
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
    icono='FotosApps/FotoAppTelefono.jpg'
    
    def __init__(self,numero, torre: Torre):
        super().__init__(numero, torre)
        self.registroDeLlamadas = deque()   #pila. con appendleft
        self.enLlamada = False              #Se cambia cuando esta en llamada a la Llamada correspondiente
        self.opciones = [('Ver contactos',self.verListaContactos,[]),
                         ('Ver contactos en particular',self.verContactosEnParticular,[]),
                         ('Llamar por teclado', self.llamarPorTeclado, []),
                         ('Llamar por contacto', self.llamarContacto, []),
                         ('Cortar llamada',self.cortarLlamada,[]),
                         ('Ver historial llamadas', self.verHistorialLlamadas,[]),
                         ('Volver a pantalla de inicio', self.volver, [])]
    
    def llamarPorTeclado(self):
        '''
        Llama a un numero de telefono mediante el teclado de la aplicacion, o sea marcando los numeros del celular a llamar.
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
                if self.torre.verificarEstado(self.nombre,self.miNumero) and self.torre.verificarEstado(self.nombre,numero): #verifica ambos numeros
                    self.enLlamada = Llamada(self.miNumero, numero)
                    self.torre.telefonosRegistrados[self.enLlamada.numReceptor].aplicaciones['Telefono'].recibirLlamada(self.enLlamada)

    def llamarContacto(self):
        '''
        Llama a un numero de telefono mediante el nombre con el que lo tiene agendado como contacto.
        Si intenta llamar a un nombre que no esta en los contactos, levanta error ya que por nombre de contacto solo
        se puede llamar a los que efectivamente son contactos
        '''
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

    def recibirLlamada(self,llamada: Llamada):
        '''
        Recibe una llamada.
        Si el numero que esta llamando esta en nuestros contactos, se muestra que la llamada es de ese nombre de contacto
        En caso contrario se muestra el numero del emisor de la llamada
        Posteriormente se procede a recibir o rechazar la llamada. Si la llamada se rechaza, no se guarda
        '''
        print(f'\n(Se esta operando el telefono: {llamada.numReceptor})')
        if llamada.numEmisor in list(map(lambda contacto: contacto.numTelefono,self.contactos.values())):
            for nombre in self.contactos:
                if self.contactos[nombre].numTelefono==llamada.numEmisor:
                    print('Llamada de', nombre)
        else:
            print('Llamada entrante de', llamada.numEmisor)
        respuesta=input('Ingrese 0 para cortar, cualquier otro caracter para aceptar: ')
        if respuesta=='0':
            self.torre.telefonosRegistrados[llamada.numEmisor].aplicaciones['Telefono'].enLlamada=False
            print('Llamada rechazada')
        else:
            self.enLlamada=llamada
            print('Llamada en curso')
            
    def registrarLlamadaTelefono(self,llamada: Llamada):
        '''
        Registra una llamada en la aplicacion Telefono
        '''
        self.registroDeLlamadas.appendleft(llamada)
    
    def registrarLlamadaTorre(self,llamada: Llamada):
        '''
        Registra una llamada en el registro de la Torre Central
        '''
        self.torre.registroDeLlamadas.append(llamada)

    def cortarLlamada(self):
        '''
        Corta una llamada.
        Si no se esta en llamada, no tendria sentido cortar la llamada entonces levanta un error
        Al terminarse la llamada, se registra en los historiales de llamada de los telefonos y de la Torre Central
        '''
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
        '''
        Recibe el corte de llamada que ejecuto la otra parte interviniente en la comunicacion
        Vuelve el estado de llamada a falso y registra la llamada
        '''
        self.enLlamada=False
        self.registrarLlamadaTelefono(llamada)
    
    def verHistorialLlamadas(self):
        '''
        Muestra las llamadas como una pila. Las mas nuevas aparecen arriba
        '''
        print('Historial de llamadas:')
        if self.registroDeLlamadas:
            for llamada in self.registroDeLlamadas:
                print(llamada)
        else:
            print('No hay llamadas registradas todavia')
        
class SMS(AplicacionComunicacion):
    nombre='SMS'
    icono='FotosApps/FotoAppSMS.jpg'
    
    def __init__(self, numero: int, torre: Torre):
        super().__init__(numero, torre)
        self.misChats={}                # {numero: objeto Chat}
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
        '''
        Crea un chat entre dos usuarios. Lo crea en la aplicacion de SMS de ambos usuario.
        '''
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
        '''
        Abre un chat por numero de telefono.
        Tira error si no se le pasa en el input un numero de telefono
        '''
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
        '''
        Abre un chat por nombre.
        '''
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
        '''
        Cierra un chat en caso de que este abierto.
        '''
        if self.chatAbierto==False:
            print('No hay un chat abierto')
        else:
            self.chatAbierto = False
            print('Se cerro el chat')
        
    def verChats(self):
        '''
        Muestra los chats.
        '''
        if self.misChats:
            for chat in list(sorted(self.misChats.values(), reverse = True)):
                print(chat)
        else:
            print('No hay chats')

    def borrarChat(self):
        '''
        Se borra el chat para los dos usuarios que intervienen en el chat, dejando asi el objeto
        Chat fuera de toda asignacion de variable
        '''
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
                self.torre.telefonosRegistrados[numero].aplicaciones['SMS'].misChats.pop(self.miNumero)
                #Aunque no suceda en la realidad, si alguien borra un chat, se elimina para ambos
                
    def enviarMensaje(self):
        '''
        Envia un mensaje si hay un chat abierto.
        '''
        if not self.chatAbierto:
            print('No hay ningun chat abierto')
        else:
            contenido=input('Ingrese el mensaje que desea enviar: ')
            self.chatAbierto.enviarMensaje(contenido, self.miNumero, self.torre)
    
    def verChatAbierto(self):
        '''
        Muestra el chat que esta abierto.
        '''
        if not self.chatAbierto:
            print('No hay ningun chat abierto')
        else:
            self.chatAbierto.verChat()
            
    def borrarMensaje(self):
        '''
        Borra un mensaje mediante su posicion.
        Previamente muestra el chat para poder ver la posicion de los mensajes
        '''
        if not self.chatAbierto:
            print('No hay ningun chat abierto')
        else:
            if self.chatAbierto.mensajes.esVacia():
                print('No hay mensajes')
            else:
                self.chatAbierto.verChat()
                try:
                    pos=int(input('Ingrese la posicion del mensaje que desea eliminar: '))
                except ValueError:
                    print('No ingreso un numero entero')
                else:
                    self.chatAbierto.borrarMensaje(pos, self.miNumero)
                
    def volver(self):
        '''
        Cuando se sale de la aplicacion, se cierran los chats en caso de que haya alguno abierto
        '''
        self.cerrarChat()
        return True