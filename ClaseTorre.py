from collections import deque

class Torre:
    
    def __init__(self):
        self.telefonosRegistrados={}        #{numero : objeto Celular}
        self.registroDeLlamadas=deque()     #Cola
        self.registroDeMensajes=deque()     #Cola    Porque quiero ver primero los mensajes mas viejos, los que llegaron primeros
        self.mensajesPendientes={} #{numero: cola de mensajes pendientes que se entregan cuando se conecta a internet}
    
    def agregarTelefono(self, celular):
        '''
        Agrega un celular a los registrados por la Torre.
        '''
        if celular.numero not in self.telefonosRegistrados:
            self.telefonosRegistrados[celular.numero]=celular
            self.mensajesPendientes[celular.numero]=deque()
        else:
            raise ValueError('Telefono ya registrado')
        
    def borrarTelefono(self, numero):
        '''
        Saca un telefono de los registrados por la Torre
        '''
        if numero not in self.telefonosRegistrados:
            raise ValueError('Telefono no registrado')
        else:
            self.telefonosRegistrados.pop(numero)
            
    def verificarEstado(self, aplicacionDeOrigen, numTelefono):
        '''
        Verifica que un usuario este disponible para comunicarse a traves de la aplicacion Telefono con una llamada
        o a traves de SMS con un mensaje
        '''
        if numTelefono in self.telefonosRegistrados:
            if self.telefonosRegistrados[numTelefono].apagado:
                print(f'Celular {numTelefono} apagado')
                return False
            if aplicacionDeOrigen=='Telefono':
                if not self.telefonosRegistrados[numTelefono].redMovil:
                    print(f'Celular {numTelefono} sin red movil')
                    return False
                elif self.telefonosRegistrados[numTelefono].aplicaciones['Telefono'].enLlamada:
                    print(f'Celular {numTelefono} ocupado')
                    return False
                return True
            elif aplicacionDeOrigen=='SMS':
                if not self.telefonosRegistrados[numTelefono].internet:
                    print(f'Celular {numTelefono} sin internet')
                    return False
                return True
        else:
            print(f'Celular {numTelefono} no registrado')
            return False
        
    def recibirMensaje(self, mensaje):
        '''
        Recibe un mensaje y lo agrega al registro de mensajes de la torre.
        Si el receptor del mensaje tiene el celular prendido y con internet, se le entrega el mensaje,
        sino, la Torre retiene el mensaje hasta que se vuelva a conectar a Internet el receptor
        '''
        self.registroDeMensajes.append(mensaje)
        if self.verificarEstado('SMS', mensaje.numReceptor): #si lo puede recibir, lo recibe
            mensaje.entregado=True
        else:                 #sino una vez que encienda el internet, quiere decir que tambien esta prendido, recibe el mensaje
            self.mensajesPendientes[mensaje.numReceptor].append(mensaje)
            
    def entregarMensajes(self, numero):
        '''
        Si el usuario tiene mensajes pendientes de ser entregados, la Torre le entrega los mensajes
        '''
        if self.mensajesPendientes[numero]:
            for mensaje in self.mensajesPendientes[numero]:
                mensaje.entregado=True
            self.mensajesPendientes[numero].clear()
            
