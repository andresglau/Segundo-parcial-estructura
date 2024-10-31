from ClaseTorre import Torre
from ClaseAplicacion import Telefono, Contactos, SMS
from ClaseAppStore import AppStore
from ClaseConfiguracion import Configuracion
from ClaseEmail import Email

class Celular:
    
    idUnicos=set()
    modelosPermitidos={'iphone 15','iphone 16','samsung s20'}
    #No se pueden repetir numeros celulares
    numerosUso=set()
    
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, numero: int, codigo: int, mail: str):
        #verificaciones
        if modelo not in self.modelosPermitidos:
            raise ValueError('modelo no permitido')
        if len(str(numero))!=10 or str(numero)[:2]!='11' or str(numero)[2]=='0' or numero<0:
            raise ValueError('numero de celular incorrecto. Debe tener el siguiente formato: 1123456789')
        if numero in self.numerosUso:
            raise ValueError('numero de celular usado')
        if len(str(codigo))!=4 or type(codigo)!=int:
            raise ValueError('Codigo incorrecto. Debe tener el siguiente formato 1234')
        if mail in Email.emailsRegistrados:           #VALIDAR ADEMAS QUE SEA UN FORMATO DE MAIL VALIDO
            raise ValueError('No puede tener ese mail. Ya lo tiene otro usuario')
            
        #instanciar
        if self.idUnicos:
            self.id=max(self.idUnicos)+1
        else:
            self.id=1000
        self.idUnicos.add(self.id)
        self.nombre=nombre
        self.modelo=modelo
        self.version = version
        self.memoriaRAM = memoriaRAM
        self.almacenamiento=almacenamiento
        self.numero=numero
        self.numerosUso.add(numero)
        self.apagado = True
        self.bloqueado = True
        #la funcion de red movil es permitir realizar una llamada. Asumimos que se activa desde el telefono ya que no sabemos como saber si el telefono en un determinado momento tiene senal o no.
        self.redMovil=False
        self.internet=False
        self.bluetooth=False
        self.modoAvion=False
        self.codigo=codigo
        self.aplicaciones={Contactos.nombre:Contactos(self.numero), Telefono.nombre:Telefono(self.numero),
                           SMS.nombre:SMS(self.numero), AppStore.nombre: AppStore(self), 
                           Configuracion.nombre:Configuracion(self), Email.nombre:Email(mail)}
        #diccionario de aplicaciones descargadas. Por defecto vienen estas, y no se pueden borrar.
        
        #linkear contactos con telefono y sms
        self.aplicaciones['Telefono'].contactos = self.aplicaciones['Contactos'].contactos
        self.aplicaciones['SMS'].contactos = self.aplicaciones['Contactos'].contactos
        self.appActiva = None
    
    #prender el telefono si esta apagado    
    def prender(self):
        if self.apagado:
            self.apagado = False
            print('Se prendio el celular')
        else:    
            raise ValueError('El celular ya esta prendido')
    
    #prender el telefono si esta prendido    
    def apagar(self):
        if not self.apagado:
            if not self.bloqueado:
                self.bloquear()
            if self.internet:
                self.desactivarInternet()
            if self.redMovil:
                self.desactivarRedMovil()
            self.apagado = True
            print('Se apago el celular')
        else:
            raise ValueError('El celular ya esta apagado')
        
    #desbloquear el telefono si esta bloqueado    
    def desbloquear(self, codigo):
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
    
    #bloquear el telefono si esta desblqueado        
    def bloquear(self):
        if not self.apagado:
            if not self.bloqueado:
                self.bloqueado = True
                print('Se bloqueo el celular')
            else:
                raise ValueError('El telefono ya esta bloqueado')
        else:
            raise ValueError('El celular esta apagado')
        
    def abrirApp(self, nombre):
        if self.appActiva != None:
            raise ValueError('Todavia esta en otra aplicacion')
        if nombre not in self.aplicaciones:
            raise ValueError('No tenes descargada esa App')
        else:
            self.appActiva = self.aplicaciones[nombre]
            # self.aplicaciones[nombre].mostrarMenu()
    
    def cerrarApp(self):
        self.appActiva = None

    def borrarAplicacion(self,nombreApp):        
        if nombreApp not in self.aplicaciones:
            raise ValueError('Esa aplicacion no se puede borrar porque no esta descargada')
        elif nombreApp not in AppStore.aplicacionesDisponibles:
            print('Es una aplicacion base, no se puede eliminar')
        else:
            self.aplicaciones.pop(nombreApp)
            print(f'Se elimino la aplicacion {nombreApp}') #creo que asi hace lo mismo en una linea print(f'Se elimino la aplicacion {self.aplicaciones.pop(nombreApp)}')

    def verAplicaciones(self): #hacer un ver pantalla
        print('Aplicaciones en el celular:')
        for nombre in self.aplicaciones:
            print(nombre)
    
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
try:
    celuAndy=Celular('Andy', 'iphone 15', '12', 12, 256, 1145672241)
    celuFede=Celular('Fede', 'iphone 15', '12', 12, 256, 1145673241)
    torreCentral = Torre()
    
    #COSAS BASICAS PARA PODER USARLO
    celuIchi = Celular('Isidro', 'iphone 15', '12', 12, 256, 1145272200)
    celuIchi.prender()
    celuIchi.desbloquear()
    
    #ABRO CONTACTOS Y OPERO
    # celuIchi.abrirApp('Contactos')
    # celuIchi.appActiva.agregarContacto('Fede', 1145673241)
    # celuIchi.appActiva.actualizarContacto('Fede', 'Fede L', 1189022331)
    # celuIchi.appActiva.eliminarContacto('Fede L')
    # celuIchi.appActiva.verListaContactos()
    # celuIchi.cerrarApp()
    
    #ABRO TELEFONO E INTENTO LLAMAR
    celuIchi.abrirApp('Telefono')
    # celuIchi.appActiva.llamarPorTeclado(1145672241, torreCentral)     ACA TODAVIA NO ESTA REGISTRADO
    torreCentral.agregarTelefono(celuAndy)
    torreCentral.agregarTelefono(celuIchi)
    celuIchi.activarRedMovil()
    #celuAndy activa lo suyo
    celuAndy.prender()
    celuAndy.activarRedMovil()
    #seguimos
    # celuIchi.appActiva.llamarPorTeclado(1145672241, torreCentral)
    # celuAndy.aplicaciones['Telefono'].cortarLlamada(torreCentral)
    # celuIchi.appActiva.cortarLlamada(torreCentral)
    celuIchi.appActiva.verHistorialLlamadas()
    
    #ABRO SMS Y MANDO MENSAJES
    # celuIchi.appActiva.crearChat(1145272200, torreCentral)

    #PRUEBO BAJAR APP
    # celuIchi.cerrarApp()
    # celuIchi.abrirApp('App Store')
    # celuIchi.appActiva.verAplicacionesDisponibles()
    # celuIchi.appActiva.descargarAplicacion('Configuracion')
    # celuIchi.cerrarApp()
    # celuIchi.abrirApp('Configuracion')
    # celuIchi.verAplicaciones()
    

except BaseException as e:
    print(e)



# alicaciones={'Telefono': 'Telefono(self.numero)'}
# celu.abrirAplicacion('Telefono')
# #self.appActiva = Telefono()
# celu.salirAplicacion()      #self.appActiva = None  
# #self.appActiva = AppStore()  
# #self.appActiva = 

# #self.telefono=Telefono(self.numero)

