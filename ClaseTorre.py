from collections import deque
class Torre:   #cambiar todos los "torre" a "central"
    
    def __init__(self):
        self.telefonosRegistrados={} #{numero,objeto}
        self.registroDeLlamadas=deque()
        self.registroDeMensajes=deque()
    
    #agregar telefono
    def agregarTelefono(self, celular): #en principio le pasamos el objeto celular como parametro
        if celular.numero not in self.telefonosRegistrados:
            self.telefonosRegistrados[celular.numero]=celular
        else:
            raise ValueError('Telefono ya registrado')
        
    #dar de baja telefono
    def borrarTelefono(self, numero):
        if numero not in self.telefonosRegistrados:
            raise ValueError('Telefono no registrado')
        else:
            self.telefonosRegistrados.pop(numero)
            
    #verificar estado
    def verificarEstado(self, aplicacionDeOrigen, numTelefono, mensaje=None): #por defecto es None por si hace llamada
        if numTelefono in self.telefonosRegistrados:
            if aplicacionDeOrigen=='Telefono':
                if self.telefonosRegistrados[numTelefono].apagado:
                    print('Celular apagado')
                    return False
                elif not self.telefonosRegistrados[numTelefono].redMovil:
                    print('Celular sin red movil')
                    return False
                elif self.telefonosRegistrados[numTelefono].aplicaciones['Telefono'].enLlamada:
                    print('Celular ocupado')
                    return False
                else:
                    return True
            elif aplicacionDeOrigen=='SMS':
                pass

        else:
            print('Celular no registrado')
            return False
