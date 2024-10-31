from ClaseAplicacion import Aplicacion
from ClaseTorre import Torre

class Configuracion(Aplicacion):
    nombre='Configuracion'
    icono=None

    def __init__(self, celular):
        self.celular=celular

    #activar red movil    
    def activarRedMovil(self):
        if not self.celular.apagado: #ver si hace falta verificar esto en todos los metodos de activar/desactivar
            if not self.celular.redMovil:
                self.celular.redMovil = True
                print('Se activo la red movil')
            else:
                raise ValueError('La red movil ya esta activada')
        else:
            raise ValueError('El celular esta apagado')
        
    #desactivar red movil
    def desactivarRedMovil(self):
        if not self.celular.apagado:
            if self.celular.redMovil:
                self.celular.redMovil = False
                print('Se desactivo la red movil')
            else:
                raise ValueError('La red movil ya esta desactivada')
        else:
            raise ValueError('El celular esta apagado')
        
    #activar internet    
    def activarInternet(self, torre:Torre):
        if not self.celular.apagado:
            if not self.celular.internet:
                self.celular.internet = True
                print('Se activo el internet')
                if self.celular.numero in torre.telefonosRegistrados: #solo los celulares que estan registrados en la torre
                    torre.entregarMensajes(self.numero) #recibe los SMS que le enviaron cuando no tenia internet
            else:
                raise ValueError('La internet ya esta activado')
        else:
            raise ValueError('El celular esta apagado')
        
    #desactivar internet
    def desactivarInternet(self):
        if not self.celular.apagado:
            if self.celular.internet:
                self.celular.internet = False
                print('Se desactivo el internet')
            else:
                raise ValueError('El internet ya esta desactivado')
        else:
            raise ValueError('El celular esta apagado')

    def activarBluetooth(self):
        if not self.celular.apagado: 
            if not self.celular.bluetooth:
                self.celular.bluetooth = True
                print('Se activo el bluetooth')
            else:
                raise ValueError('El bluetooth ya esta activada')
        else:
            raise ValueError('El celular esta apagado')
        
    def desactivarRedMovil(self):
        if not self.celular.apagado:
            if self.celular.bluetooth:
                self.celular.bluetooth = False
                print('Se desactivo el bluetooth')
            else:
                raise ValueError('El bluetooth ya esta desactivado')
        else:
            raise ValueError('El celular esta apagado')
    
    def activarModoAvion(self):
        if not self.celular.apagado:
            if not self.celular.modoAvion:
                self.celular.modoAvion = True
                print('Se activo el modo avion')
            else:
                raise ValueError('El modo avion ya esta activado')
        else:
            raise ValueError('El celular esta apagado')
        
    def desactivarModoAvion(self):
        if not self.celular.apagado:
            if self.celular.modoAvion:
                self.celular.modoAvion = False
                print('Se desactivo el modo avion')
            else:
                raise ValueError('El modo avion ya esta desactivada')
        else:
            raise ValueError('El celular esta apagado')
        
    def cambiarCodigo(self, codigo): # si da el tiempo agregar que me pida el codigo antes de cambiarlo
        if len(str(codigo))!=4 or type(codigo)!=int:
            raise ValueError('Codigo incorrecto. Debe tener el siguiente formato 1234')
        elif codigo==self.celular.codigo:
            print('Debe poner un codigo distinto al que ya tenia')
        else:
            self.celular.codigo=codigo

    def cambiarNombre(self, nombre):
        self.celular.nombre=nombre