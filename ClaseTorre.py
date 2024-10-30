from collections import deque

class Torre:   #cambiar todos los "torre" a "central"
    
    def __init__(self):
        self.telefonosRegistrados={} #{numero,objeto}
        self.registroDeLlamadas=deque()     #O lista secuencial?
        self.registroDeMensajes=deque()
        self.mensajesPendientes={} #diccionaro {numero: cola de mensajes pendientes que se entregan cuando se conecta a internet}
    
    #agregar telefono
    def agregarTelefono(self, celular): #en principio le pasamos el objeto celular como parametro
        if celular.numero not in self.telefonosRegistrados:
            self.telefonosRegistrados[celular.numero]=celular
            self.mensajesPendientes[celular.numero]=deque()
        else:
            raise ValueError('Telefono ya registrado')
        
    #dar de baja telefono
    def borrarTelefono(self, numero):
        if numero not in self.telefonosRegistrados:
            raise ValueError('Telefono no registrado')
        else:
            self.telefonosRegistrados.pop(numero)
            
    #verificar estado
    def verificarEstado(self, aplicacionDeOrigen, numTelefono):
        if numTelefono in self.telefonosRegistrados:
            if aplicacionDeOrigen=='Telefono':
                if self.telefonosRegistrados[numTelefono].apagado:
                    print(f'Celular {numTelefono} apagado')
                    return False
                elif not self.telefonosRegistrados[numTelefono].redMovil:
                    print(f'Celular {numTelefono} sin red movil')
                    return False
                elif self.telefonosRegistrados[numTelefono].aplicaciones['Telefono'].enLlamada:
                    print(f'Celular {numTelefono} ocupado')
                    return False
                return True
            elif aplicacionDeOrigen=='SMS':
                if self.telefonosRegistrados[numTelefono].apagado:      #SE REPITE
                    print(f'Celular {numTelefono} apagado')
                    return False
                elif not self.telefonosRegistrados[numTelefono].internet:
                    print(f'Celular {numTelefono} sin internet')
                    return False
                return True

        else:
            print(f'Celular {numTelefono} no registrado')
            return False
        
    def recibirMensaje(self, mensaje):
        self.registroDeMensajes.append(mensaje)
        if self.verificarEstado('SMS',mensaje.numReceptor): #si lo puede recibir, lo recibe
            mensaje.entregado=True
        else: #sino una vez que encienda el internet, quiere decir que tambien esta prendido, recibe el mensaje
            self.mensajesPendientes[mensaje.numReceptor].append(mensaje)
            
    def entregarMensajes(self, numero):
        if self.mensajesPendientes[numero]:
            for mensaje in self.mensajesPendientes[numero]:
                mensaje.entregado=True
            self.mensajesPendientes[numero].clear()
            
