from ClaseTorre import Torre
from ClaseAplicacion import Telefono, Contactos, SMS
from ClaseAppStore import AppStore
from ClaseConfiguracion import *
from ClaseEmail import Email

class DispositivoElectronico:
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.modelo = modelo
        self.version = version
        self.memoriaRAM = memoriaRAM
        self.almacenamiento = almacenamiento
        self.apagado = True
        self.bloqueado = True
        self.internet=False   #Un celular viejo va a poder acceder a Internet por la configuracion previa del programa donde para usar SMS se requiere Internet (unicamente con ese uso)
        self.modoAvion = False
        self.aplicaciones = {Configuracion.nombre: Configuracion()}

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
    
    def apagar(self):
        '''
        El celular cambia su estado de prendido.
        Cuando se apaga el celular, en caso de tener alguna de estas funcionalidades activadas, se bloquea y desactiva
        el modo avion
        Si esta apagado, levanta un error
        '''
        if not self.apagado:
            if not self.bloqueado:
                self.bloquear()
            if self.internet:
                self.internet = False
            if self.modoAvion:
                self.modoAvion = False
            self.apagado = True
            print('Se apago el celular')
        else:
            raise ValueError('El celular ya esta apagado')

    def desbloquear(self):
        '''
        Desbloquea el celular.
        '''
        try:
            if not self.apagado:
                if self.bloqueado:
                    self.bloqueado = False
                    print('Se desbloqueo el celular')
                else:
                    raise ValueError('El telefono ya esta desbloqueado')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)

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
    
    def verAplicaciones(self):
        '''
        Muestra la pantalla del celular con las aplicaciones del mismo
        '''
        print('Aplicaciones en el celular:')
        for nombre in self.aplicaciones:
            print('\t'+nombre)

    def __str__(self):
        return f'El dispositivo electronico de {self.nombre} modelo {self.modelo}'
    
    def __repr__(self):
        return self.__str__()



class DispositivoConRedMovil(DispositivoElectronico):
    
    numerosUso = dict() #No se pueden repetir numeros celulares

    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, numero: int, torre: Torre, **kwargs):
        super().__init__(nombre, modelo, version, memoriaRAM, almacenamiento, **kwargs)
        self.numero = numero
        DispositivoConRedMovil.numerosUso[numero]=self
        self.aplicaciones.update({Contactos.nombre:Contactos(self.numero,torre), Telefono.nombre:Telefono(self.numero,torre),
                        SMS.nombre:SMS(self.numero, torre)})
        #La funcion de red movil es permitir realizar una llamada.
        self.redMovil=False
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
        
    def apagar(self):
        '''
        El celular cambia su estado de prendido.
        Cuando se apaga el celular, en caso de tener alguna de estas funcionalidades activadas, se bloquea,
        desactiva la red movil, desactiva el internet y corta las llamadas en caso que haya
        Si esta apagado, levanta un error
        '''
        if not self.apagado:
            if not self.bloqueado:
                self.bloquear()
            if self.redMovil:
                self.redMovil = False
            if self.modoAvion:
                self.modoAvion = False
            if self.aplicaciones['Telefono'].enLlamada!=False:
                self.aplicaciones['Telefono'].cortarLlamada()
            self.apagado = True
            print('Se apago el celular')
        else:
            raise ValueError('El celular ya esta apagado')
        
    def __str__(self):
        return f'El celular de {self.nombre} modelo {self.modelo} tiene numero de celular {self.numero}'
    
    def __repr__(self):
        return self.__str__()

class DispositivoInteligente(DispositivoElectronico):
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, codigo: int, mail: str, **kwargs):
        super().__init__(nombre, modelo, version, memoriaRAM, almacenamiento, **kwargs)
        self.aplicaciones.update({AppStore.nombre: AppStore(self), Email.nombre:Email(mail)})
        #Diccionario de aplicaciones descargadas. Por defecto vienen estas a los dispositivos inteligentes

        self.bluetooth=False
        self.codigo=codigo
    
    def apagar(self):
        '''
        El celular cambia su estado de prendido.
        Cuando se apaga el celular, en caso de tener alguna de estas funcionalidades activadas, se bloquea,
        desactiva el internet y desactiva el modo avion
        Si esta apagado, levanta un error
        '''
        if not self.apagado:
            if not self.bloqueado:
                self.bloquear()
            if self.internet:
                self.internet = False
            if self.bluetooth:
                self.bluetooth = False
            if self.modoAvion:
                self.modoAvion = False
            self.apagado = True
            print('Se apago el celular')
        else:
            raise ValueError('El celular ya esta apagado')
    
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
            print(f'Se elimino la aplicacion {nombreApp}')

    def get_mail(self):
        return self.aplicaciones['Email'].miMail
    
    def __str__(self):
        return f'El dispositivo con internet de {self.nombre} modelo {self.modelo}'
    
    def __repr__(self):
        return self.__str__()

class Celular(DispositivoInteligente, DispositivoConRedMovil):
    idUnicos=set()
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, numero: int, codigo: int, mail: str, torre: Torre, **kwargs):
        '''Se instancia el celular con sus respectivos atributos y modificaciones a los atributos de la clase Celular'''
        super().__init__(nombre=nombre, modelo=modelo, version=version, memoriaRAM=memoriaRAM, almacenamiento=almacenamiento, codigo=codigo, mail=mail, numero=numero, torre=torre, **kwargs)
        if self.idUnicos:
            self.id=max(self.idUnicos)+1
        else:
            self.id=1000
        self.idUnicos.add(self.id)
        self.aplicaciones.update({ConfiguracionCelular.nombre:ConfiguracionCelular(self, torre)})
    
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
    
    def __str__(self):
        return f'El celular de {self.nombre} modelo {self.modelo} tiene numero de celular {self.numero}'
    
    def __repr__(self):
        return self.__str__()
    
class CelularAntiguo(DispositivoConRedMovil):
    idUnicos=set()
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, numero: int, torre: Torre):
        super().__init__(nombre, modelo, version, memoriaRAM, almacenamiento, numero, torre)
        if self.idUnicos:
            self.id=max(self.idUnicos)+1
        else:
            self.id=1000
        self.idUnicos.add(self.id)
        self.aplicaciones.update({ConfiguracionCelularViejo.nombre:ConfiguracionCelularViejo(self, torre)})
        
class Tablet(DispositivoInteligente):
    idUnicos=set()
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, codigo: int, mail: str):
        super().__init__(nombre, modelo, version, memoriaRAM, almacenamiento, codigo, mail)
        if self.idUnicos:
            self.id=max(self.idUnicos)+1
        else:
            self.id=1000
        self.idUnicos.add(self.id)
        self.aplicaciones.update({ConfiguracionTablet.nombre:ConfiguracionTablet()})
    
    def __str__(self):
        return f'La tablet de {self.nombre} modelo {self.modelo}'
    
    def __repr__(self):
        return self.__str__()