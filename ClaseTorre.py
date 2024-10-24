class Torre:
    
    def __init__(self):
        self.telefonosRegistrados={} #{numero,objeto}
        self.registroDeLlamadas=[]
        self.registroDeMensajes=[]
    
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
    def verificarEstado(self, aplicacionDeOrigen, numeroDeDestino, mensaje=None): #por defecto es None por si hace llamada
        if numeroDeDestino in self.telefonosRegistrados:
            if aplicacionDeOrigen=='telefono':
                if self.telefonosRegistrados[numeroDeDestino].apagado:
                    print('Celular apagado')
                    return False
                elif not self.telefonosRegistrados[numeroDeDestino].redMovil:
                    print('Celular sin red movil')
                    return False
                elif self.telefonosRegistrados[numeroDeDestino].aplicaciones['telefono'].enLlamada:
                    print('Celular ocupado')
                    return False
                else:
                    return True
            elif aplicacionDeOrigen=='SMS':
                pass

        else:
            print('Celular no registrado')
            return False
