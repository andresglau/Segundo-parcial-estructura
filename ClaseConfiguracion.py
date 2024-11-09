from ClaseAplicacion import Aplicacion
from ClaseTorre import Torre

class Configuracion(Aplicacion):
    nombre='Configuracion'
    icono=None

    def __init__(self, celular, torre: Torre):
        super().__init__()
        self.celular=celular
        self.torre = torre
        self.opciones = [('Activar red movil', self.activar, ['red movil']),
                         ('Desactivar red movil',self.desactivar,['red movil']),
                         ('Activar internet', self.activar, ['internet']),
                         ('Desactivar internet', self.desactivar,['internet']),
                         ('Activar Bluetooth', self.activar, ['bluetooth']),
                         ('Desactivar Bluetooth', self.desactivar,['bluetooth']),
                         ('Activar modo avion', self.activar, ['modo avion']),
                         ('Desactivar modo avion', self.desactivar, ['modo avion']),
                         ('Cambiar codigo de desbloqueo', self.cambiarCodigo,[]),
                         ('Cambiar nombre del telefono', self.cambiarNombre, []),
                         ('Volver a pantalla de inicio', self.volver, [])]
    def activar(self, nombre: str):
        '''
        Activa la funcionalidad que se le pasa como parametro.
        Antes que nada chequea que este prendido el celular
        Para poder activar Red Movil, Modo Avion debe estar desactivado. Si se activa Modo Avion, se desactiva la Red Movil
        Cuando se activa el Internet, se entregan los mensajes que estaba reteniendo la Torre Central
        '''
        try:
            if not self.celular.apagado:
                if nombre=='red movil':
                    if not self.celular.redMovil:
                        if not self.celular.modoAvion:
                            self.celular.redMovil = True
                            print('Se activo la red movil')
                        else:
                            print('No podes usar la red movil en modo avion')
                    else:
                        raise ValueError('La red movil ya esta activada')
                elif nombre=='internet':
                    if not self.celular.internet:
                        self.celular.internet = True
                        print('Se activo el internet')
                        if self.celular.numero in self.torre.telefonosRegistrados: #solo para los celulares que estan registrados en la torre
                            self.torre.entregarMensajes(self.celular.numero) #recibe los SMS que le enviaron cuando no tenia internet
                    else:
                        raise ValueError('La internet ya esta activado')
                elif nombre=='bluetooth':
                    if not self.celular.bluetooth:
                        self.celular.bluetooth = True
                        print('Se activo el bluetooth')
                    else:
                        raise ValueError('El bluetooth ya esta activada')
                elif nombre=='modo avion':
                    if not self.celular.modoAvion:
                        self.celular.modoAvion = True
                        print('Se activo el modo avion')
                        self.desactivar('red movil')
                    else:
                        raise ValueError('El modo avion ya esta activado')    
            else:
                raise ValueError('El celular esta apagado')
        except ValueError as e:
            print(e)
    
    def desactivar(self, nombre: str):
        '''
        Desactiva la funcionalidad que se le pasa como parametro.
        '''
        try:
            if not self.celular.apagado:
                if nombre == 'red movil':
                    if self.celular.redMovil:
                        self.celular.redMovil = False
                        print('Se desactivo la red movil')
                    else:
                        raise ValueError('La red movil ya esta desactivada')
                elif nombre == 'internet':
                    if self.celular.internet:
                        self.celular.internet = False
                        print('Se desactivo el internet')
                    else:
                        raise ValueError('El internet ya esta desactivado')
                elif nombre == 'bluetooth':
                    if self.celular.bluetooth:
                        self.celular.bluetooth = False
                        print('Se desactivo el bluetooth')
                    else:
                        raise ValueError('El bluetooth ya esta desactivado')
                elif nombre == 'modo avion':
                    if self.celular.modoAvion:
                        self.celular.modoAvion = False
                        print('Se desactivo el modo avion')
                    else:
                        raise ValueError('El modo avion ya esta desactivado')
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