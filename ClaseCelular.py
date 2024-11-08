from ClaseTorre import Torre
from ClaseAplicacion import Telefono, Contactos, SMS
from ClaseAppStore import AppStore
from ClaseConfiguracion import Configuracion
from ClaseEmail import Email

class Celular:
    
    idUnicos=set()
    # modelosPermitidos={'iphone 15','iphone 16','samsung s20'} YA ESTA EN EL MENU
    numerosUso = dict() #No se pueden repetir numeros celulares
    
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, numero: int, codigo: int, mail: str, torre: Torre):
        '''Se instancia el celular con sus respectivos atributos y modificaciones a los atributos de la clase Celular'''
        if self.idUnicos:
            self.id=max(self.idUnicos)+1
        else:
            self.id=1000
        self.idUnicos.add(self.id)
        self.nombre = nombre
        self.modelo = modelo
        self.version = version
        self.memoriaRAM = memoriaRAM
        self.almacenamiento = almacenamiento
        self.numero = numero
        Celular.numerosUso[numero]=self
        self.apagado = True
        self.bloqueado = True
        #La funcion de red movil es permitir realizar una llamada.
        self.redMovil=False
        self.internet=False
        self.bluetooth=False
        self.modoAvion=False
        self.codigo=codigo
        self.aplicaciones={Contactos.nombre:Contactos(self.numero,torre), Telefono.nombre:Telefono(self.numero,torre),
                           SMS.nombre:SMS(self.numero, torre), AppStore.nombre: AppStore(self), 
                           Configuracion.nombre:Configuracion(self, torre), Email.nombre:Email(mail)}
        #Diccionario de aplicaciones descargadas. Por defecto vienen estas, y no se pueden borrar.
        '''
        Abajo se sincronizan los contactos de las Apps de Comunicacion. Por default, una app de comunicacion tiene
        una lista de contactos. Como estas aplicaciones estan el mismo celular, el celular al crearse sincroniza las
        respectivas listas de contacto
        '''
        self.aplicaciones['Telefono'].contactos = self.aplicaciones['Contactos'].contactos
        self.aplicaciones['SMS'].contactos = self.aplicaciones['Contactos'].contactos
        '''
        El telefono se da de alta en la torre. Asumimos que en nuestra forma de interactuar con el programa,
        un telefono simepre va a estar en la torre, aunque no suceda asi en la realidad. De igual manera,
        existe el metodo dar de baja a un celular en la torre
        '''
        torre.agregarTelefono(self)
    
    #prender el telefono si esta apagado    
    def prender(self):
        '''
        El celular cambia su estado de apagado.
        Si esta prendido, no tiene logica prenderlo, por ende, levanta un error
        '''
        if self.apagado:
            self.apagado = False
            print('Se prendio el celular')
        else:    
            raise ValueError('El celular ya esta prendido')
    
    #prender el telefono si esta prendido    
    def apagar(self):
        '''
        El celular cambia su estado de prendido.
        Cuando se apaga el celular, en caso de tener alguna de estas funcionalidades activadas, se bloquea,
        desactiva el internet y desactiva la red movil
        Si esta apagado, levanta un error
        '''
        if not self.apagado:
            if not self.bloqueado:
                self.bloquear()
            if self.internet:
                self.internet = False
            if self.redMovil:
                self.redMovil = False
            if self.bluetooth:
                self.bluetooth = False
            if self.modoAvion:
                self.modoAvion = False
            if self.aplicaciones['Telefono'].enLlamada!=False:
                self.aplicaciones['Telefono'].cortarLlamada()
            self.apagado = True
            print('Se apago el celular')
        else:
            raise ValueError('El celular ya esta apagado')
        
    #desbloquear el telefono si esta bloqueado    
    def desbloquear(self):
        '''
        Desbloquea el celular pero solo si ingreso la clave correcta.
        Si fallo en la clave muestra un mensaje, pero si el telefono ya esta desbloqueado o apagado, levanta un error
        '''
        try:
            codigo=int(input('Ingrese el codigo de desbloqueo: '))
        except ValueError:
            print('Debe ingresar un numero')
        else:
            try:
                if not self.apagado:
                    if self.bloqueado:
                        if codigo==self.codigo:
                            self.bloqueado = False
                            print('Se desbloqueo el celular')
                        else:
                            print('Codigo incorrecto')
                    else:
                        raise ValueError('El telefono ya esta desbloqueado')
                else:
                    raise ValueError('El celular esta apagado')
            except ValueError as e:
                print(e)
    
    #bloquear el telefono si esta desblqueado        
    def bloquear(self):
        '''
        Bloquea el celular.
        Si el telefono ya esta bloqueado o apagado, levanta un error
        '''
        if not self.apagado:
            if not self.bloqueado:
                self.bloqueado = True
                print('Se bloqueo el celular')
            else:
                raise ValueError('El telefono ya esta bloqueado')
        else:
            raise ValueError('El celular esta apagado')

    def borrarAplicacion(self):
        '''
        Borra una aplicacion que le ingrese el usuario.
        Si la aplicacion no esta descargada, levanta un error
        Si la aplicacion viene con el celular, muestra un mensaje de que no puede eliminarse
        '''
        nombreApp=input('Ingrese el nombre de la aplicacion a borrar: ')
        if nombreApp not in self.aplicaciones:
            raise ValueError('Esa aplicacion no se puede borrar porque no esta descargada')
        elif nombreApp not in AppStore.aplicacionesDisponibles:
            print('Es una aplicacion base, no se puede eliminar')
        else:
            self.aplicaciones.pop(nombreApp)
            print(f'Se elimino la aplicacion {nombreApp}') #creo que asi hace lo mismo en una linea print(f'Se elimino la aplicacion {self.aplicaciones.pop(nombreApp)}')

    def verAplicaciones(self):
        '''
        Muestra la pantalla del celular con las aplicaciones del mismo
        '''
        print('Aplicaciones en el celular:')
        for nombre in self.aplicaciones:
            print('\t'+nombre)
    
    def get_nombre(self):
        return self.nombre
    
    def get_modelo(self):
        return self.modelo
    
    def get_version(self):
        return self.version

    def get_memoriaRAM(self):
        return self.memoriaRAM

    def get_almacenamiento(self):
        return self.almacenamiento

    def get_numero(self):
        return self.numero

    def get_codigo(self):
        return self.codigo

    def get_mail(self):
        return self.aplicaciones['Email'].miMail
    
    def __str__(self):
        return f'El celular de {self.nombre} modelo {self.modelo} tiene numero de celular {self.numero}'

#MAIN
# torre=Torre()
# celu = Celular('Isidro', 'iphone 15', 'iOS 7.1', 150, 64, 1156789023)
# try:
#     celu.desbloquear()
# except ValueError as e:
#     print(e)

# try:
#     celu.apagar()
# except ValueError as e:
#     print(e)

# try:
#     celu.bloquear()
# except ValueError as e:
#     print(e)
    
# celu.prender()
# celu.desbloquear()
# celu.activarInternet(torre)
# celu.activarRedMovil()

# celu2 = Celular('Andres', 'iphone 15', 'iOS 7.1', 150, 64, 1167671659)
# celu2.prender()
# celu2.activarInternet(torre)
# celu2.activarRedMovil()

# torre.agregarTelefono(celu)
# torre.agregarTelefono(celu2)

# celu2.aplicaciones['Contactos'].agregarContacto('isidro',1156789023)
# celu.aplicaciones['Telefono'].llamarPorTeclado(1167671659,torre)
# a=input('hola')
# celu.aplicaciones['Telefono'].cortarLlamada(torre)
# print(celu.aplicaciones['Telefono'].registroDeLlamadas, end = '\n')
# print(celu2.aplicaciones['Telefono'].registroDeLlamadas, end = '\n')
# print(torre.registroDeLlamadas)

# celu.aplicaciones['SMS'].crearChat(1167671659,torre)

# celu2.aplicaciones['SMS'].abrirChatPorNombre('isidro')
# celu2.aplicaciones['SMS'].chatAbierto.enviarMensaje('MENSAJE',celu.numero,torre)


# celu2.aplicaciones['SMS'].verChats()


# celu.desactivarInternet()

# celu2.aplicaciones['SMS'].chatAbierto.enviarMensaje('Estas sin internet',celu.numero,torre)

# celu.activarInternet(torre)

# celu2.aplicaciones['SMS'].chatAbierto.verChat()


#PROBANDO MAIN2
# try:
#     celuAndy=Celular('Andy', 'iphone 15', '12', 12, 256, 1145672241)
#     celuFede=Celular('Fede', 'iphone 15', '12', 12, 256, 1145673241)
#     torreCentral = Torre()
    
#     #COSAS BASICAS PARA PODER USARLO
#     celuIchi = Celular('Isidro', 'iphone 15', '12', 12, 256, 1145272200)
#     celuIchi.prender()
#     celuIchi.desbloquear()
    
#     #ABRO CONTACTOS Y OPERO
#     # celuIchi.abrirApp('Contactos')
#     # celuIchi.appActiva.agregarContacto('Fede', 1145673241)
#     # celuIchi.appActiva.actualizarContacto('Fede', 'Fede L', 1189022331)
#     # celuIchi.appActiva.eliminarContacto('Fede L')
#     # celuIchi.appActiva.verListaContactos()
#     # celuIchi.cerrarApp()
    
#     #ABRO TELEFONO E INTENTO LLAMAR
#     celuIchi.abrirApp('Telefono')
#     # celuIchi.appActiva.llamarPorTeclado(1145672241, torreCentral)     ACA TODAVIA NO ESTA REGISTRADO
#     torreCentral.agregarTelefono(celuAndy)
#     torreCentral.agregarTelefono(celuIchi)
#     celuIchi.activarRedMovil()
#     #celuAndy activa lo suyo
#     celuAndy.prender()
#     celuAndy.activarRedMovil()
#     #seguimos
#     # celuIchi.appActiva.llamarPorTeclado(1145672241, torreCentral)
#     # celuAndy.aplicaciones['Telefono'].cortarLlamada(torreCentral)
#     # celuIchi.appActiva.cortarLlamada(torreCentral)
#     celuIchi.appActiva.verHistorialLlamadas()
    
#     #ABRO SMS Y MANDO MENSAJES
#     # celuIchi.appActiva.crearChat(1145272200, torreCentral)

#     #PRUEBO BAJAR APP
#     # celuIchi.cerrarApp()
#     # celuIchi.abrirApp('App Store')
#     # celuIchi.appActiva.verAplicacionesDisponibles()
#     # celuIchi.appActiva.descargarAplicacion('Configuracion')
#     # celuIchi.cerrarApp()
#     # celuIchi.abrirApp('Configuracion')
#     # celuIchi.verAplicaciones()
    

# except BaseException as e:
#     print(e)



# # alicaciones={'Telefono': 'Telefono(self.numero)'}
# # celu.abrirAplicacion('Telefono')
# # #self.appActiva = Telefono()
# # celu.salirAplicacion()      #self.appActiva = None  
# # #self.appActiva = AppStore()  
# # #self.appActiva = 

# # #self.telefono=Telefono(self.numero)

