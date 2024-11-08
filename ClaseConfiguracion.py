from ClaseAplicacion import Aplicacion
from ClaseTorre import Torre

class Configuracion(Aplicacion):
    nombre='Configuracion'
    icono=None

    def __init__(self, celular, torre: Torre):
        super().__init__()
        self.celular=celular
        self.torre = torre
        self.opciones = [('Activar red movil', self.activarRedMovil, []),
                         ('Desactivar red movil',self.desactivarRedMovil,[]),
                         ('Activar internet', self.activarInternet, []),
                         ('Desactivar internet', self.desactivarInternet,[]),
                         ('Activar Bluetooth', self.activarBluetooth, []),
                         ('Desactivar Bluetooth', self.desactivarBluetooth,[]),
                         ('Activar modo avion', self.activarModoAvion, []),
                         ('Desactivar modo avion', self.desactivarModoAvion, []),
                         ('Cambiar codigo de desbloqueo', self.cambiarCodigo,[]),
                         ('Cambiar nombre del telefono', self.cambiarNombre, []),
                         ('Volver a pantalla de inicio', self.volver, [])]
        
    #activar red movil    
    def activarRedMovil(self):
        '''
        Activa la Red Movil.
        Si ya esta activado tira error, porque no tiene sentido activar algo activo
        '''
        try:
            if not self.celular.apagado: #ver si hace falta verificar esto en todos los metodos de activar/desactivar
                if not self.celular.redMovil:
                    self.celular.redMovil = True
                    print('Se activo la red movil')
                else:
                    raise ValueError('La red movil ya esta activada')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
        
    #desactivar red movil
    def desactivarRedMovil(self):
        '''
        Desactiva la Red Movil.
        Si ya esta desactivado tira error, porque no tiene sentido desactivar algo desactivado
        '''
        try:
            if not self.celular.apagado:
                if self.celular.redMovil:
                    self.celular.redMovil = False
                    print('Se desactivo la red movil')
                else:
                    raise ValueError('La red movil ya esta desactivada')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
        
    #activar internet    
    def activarInternet(self):
        '''
        Activa el Internet y entrega los mensajes que retuvo la Torre mientras el Internet estuvo desactivado.
        Si ya esta activado tira error, porque no tiene activar algo activo
        '''
        try:
            if not self.celular.apagado:
                if not self.celular.internet:
                    self.celular.internet = True
                    print('Se activo el internet')
                    if self.celular.numero in self.torre.telefonosRegistrados: #solo los celulares que estan registrados en la torre
                        self.torre.entregarMensajes(self.celular.numero) #recibe los SMS que le enviaron cuando no tenia internet
                else:
                    raise ValueError('La internet ya esta activado')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
        
    def desactivarInternet(self):
        '''
        Desactiva el Internet.
        Si ya esta desactivado tira error, porque no tiene sentido desactivar algo desactivado
        '''
        try:
            if not self.celular.apagado:
                if self.celular.internet:
                    self.celular.internet = False
                    print('Se desactivo el internet')
                else:
                    raise ValueError('El internet ya esta desactivado')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)

    def activarBluetooth(self):
        '''
        Activa el Bluetooth.
        Si ya esta activado tira error, porque no tiene sentido activar algo activo
        '''
        try:
            if not self.celular.apagado: 
                if not self.celular.bluetooth:
                    self.celular.bluetooth = True
                    print('Se activo el bluetooth')
                else:
                    raise ValueError('El bluetooth ya esta activada')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
        
    def desactivarBluetooth(self):
        '''
        Desactiva el Bluetooth.
        Si ya esta desactivado tira error, porque no tiene sentido desactivar algo desactivado
        '''
        try:
            if not self.celular.apagado:
                if self.celular.bluetooth:
                    self.celular.bluetooth = False
                    print('Se desactivo el bluetooth')
                else:
                    raise ValueError('El bluetooth ya esta desactivado')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
    
    def activarModoAvion(self):
        '''
        Activa el Modo Avion.
        Si ya esta activado tira error, porque no tiene sentido activar algo act
        '''
        try:
            if not self.celular.apagado:
                if not self.celular.modoAvion:
                    self.celular.modoAvion = True
                    print('Se activo el modo avion')
                else:
                    raise ValueError('El modo avion ya esta activado')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
        
    def desactivarModoAvion(self):
        '''
        Desactiva el Modo Avion.
        Si ya esta desactivado tira error, porque no tiene sentido desactivar algo desactivado
        '''
        try:
            if not self.celular.apagado:
                if self.celular.modoAvion:
                    self.celular.modoAvion = False
                    print('Se desactivo el modo avion')
                else:
                    raise ValueError('El modo avion ya esta desactivada')
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
        
    def cambiarCodigo(self):
        '''
        Cambia el codigo del celular.
        Primero pide el codigo actual para validar que el usuario que esta cambiando el codigo no sea una persona ajena al celular.
        Posteriormente renueva el codigo, validando el formato correspondiente
        '''
        try:
            codigoViejo=input('Ingrese el codigo viejo: ')
            if codigoViejo!=str(self.celular.codigo):
                print('Codigo incorrecto')
            else:
                codigo=input('Ingrese el nuevo codigo:')
                if len(codigo)!=4 or not codigo.isdigit():
                    raise ValueError('Formato incorrecto. Debe tener el siguiente formato: 1234')
                elif int(codigo)==self.celular.codigo:
                    print('Debe poner un codigo distinto al que ya tenia')
                else:
                    self.celular.codigo=int(codigo)
                    print('Se cambio el codigo')
        except ValueError as e:
            print(e)

    def cambiarNombre(self):
        '''
        Cambia el nombre del telefono.
        '''
        nombre = input('Ingrese el nuevo nombre del telefono: ')
        self.celular.nombre = nombre