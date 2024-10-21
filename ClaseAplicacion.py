from collections import deque
from ClaseTorre import Torre        
        

class Aplicacion:
    
    aplicacionesDisponibles={}
    
    def __init__(self):
        pass
    
class Telefono(Aplicacion):
    nombre='telefono'
    icono=None
    
    def __init__(self,numero):
        self.miNumero=numero
        self.contactos={} #{nombre:numero}
        self.registroDeLlamadas=deque() #cola. ordenada de anterior a reciente
        self.enLlamada=False #y se cambia cuando esta en llamada
    
    #agregar contacto. no hace falta verificar que exista ya que es lo que uno tiene agendado
    def agregarContacto(self, nombre, numero):
        if nombre not in self.contactos:
            self.contactos[nombre]=numero
        else:
            raise ValueError('Nombre ya utilizado') #no se pueden tener 2 contactos con el mismo nombre
        
    #eliminar contacto
    def eliminarContacto(self, nombre):
        if nombre not in self.contactos:
            raise ValueError('No existe este contacto')
        else:
            self.contactos.pop(nombre)
    
    #actualizar contacto        
    def actualizarContacto(self, nombre, numero):
        if nombre not in self.contactos:
            raise ValueError('No existe este contacto')
        else:
            self.contactos[nombre]=numero
    
    #verContactos
    def verContactos(self):
        for nombre in list(sorted(self.contactos.keys())):
            print(nombre, end=' ')
            
    #llamar por teclado       
    def llamar(self,numero,torre):
        if isinstance(torre,Torre): #pregunta a la torre si está disponible. si esta prendido y no está en otra llamada
            if torre.verificarEstado(self.nombre,numero):
                self.enLlamada=numero
                torre.telefonosRegistrados[numero].recibirLlamada(self.miNumero, torre)
                
    #recibir llamada
    def recibirLlamada(self,numero,torre):
        if numero in self.contactos.values():
            for nombre in self.contactos.keys():
                if self.contactos[nombre]==numero:
                    print('Llamada de',nombre)
        else:
            print('llamada de',numero)
        aceptar=input('ingrese 0 para cortar, cualquier otro caracter para aceptar: ')
        if aceptar==0:
            torre.telefonosRegistrados[numero].enLlamada=False
        else:
            self.enLlamada=numero
        


#main


telefono=Telefono(1161577917)
telefono.agregarContacto('andres',1167671659)
telefono.agregarContacto('federico',1167671658)
telefono.agregarContacto('isidro',1167671655)
telefono.agregarContacto('manuel',1167671698)

telefono.actualizarContacto('manuel',1165432345)

telefono.eliminarContacto('isidro')

telefono.verContactos()

telefono2=Telefono(1160276087)