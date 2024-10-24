from ClaseTorre import Torre
from ClaseAplicacion import *
from ClaseAplicacion import Telefono, Contactos

class Celular:
    
    idUnicos=set()
    modelosPermitidos={'iphone 15','iphone 16','samsung s20'}
    #No se pueden repetir numeros celulares
    numerosUso=set()
    
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, numero: int):
        #verificaciones
        if modelo not in self.modelosPermitidos:
            raise ValueError('modelo no permitido')
        if len(str(numero))!=10 or str(numero)[:2]!='11' or str(numero)[2]=='0' or numero<0:
            raise ValueError('numero de celular incorrecto. Debe tener el siguiente formato: 1123456789')
        if numero in self.numerosUso:
            raise ValueError('numero de celular usado')
            
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
        self.aplicaciones={'Contactos':Contactos(),'Telefono':Telefono(self.numero)}
        #linkear contactos con telefono y sms
        self.aplicaciones['Telefono'].contactos=self.aplicaciones['Contactos'].contactos
        #self.aplicaciones['SMS'].contactos=self.aplicaciones['contactos'].contactos
    
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
            self.apagado = True
            print('Se apago el celular')
        else:
            raise ValueError('El celular ya esta apagado')
        
    #desbloquear el telefono si esta bloqueado    
    def desbloquear(self):
        if not self.apagado:
            if self.bloqueado:
                self.bloqueado = False
                print('Se desbloqueo el celular')
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
    
    #activar red movil    
    def activarRedMovil(self):
        if not self.apagado:
            if not self.redMovil:
                self.redMovil = True
                print('Se activo la red movil')
            else:
                raise ValueError('La red movil ya esta activada')
        else:
            raise ValueError('El celular esta apagado')
        
    #desactivar red movil
    def desactivarRedMovil(self):
        if not self.apagado:
            if self.redMovil:
                self.redMovil = False
                print('Se desactivo la red movil')
            else:
                raise ValueError('La red movil ya esta desactivada')
        else:
            raise ValueError('El celular esta apagado')
        
    #activar internet    
    def activarInternet(self):
        if not self.apagado:
            if not self.internet:
                self.internet = True
                print('Se activo el internet')
            else:
                raise ValueError('La internet ya esta activado')
        else:
            raise ValueError('El celular esta apagado')
        
    #desactivar internet
    def desactivarInternet(self):
        if not self.apagado:
            if self.internet:
                self.internet = False
                print('Se desactivo el internet')
            else:
                raise ValueError('El internet ya esta desactivado')
        else:
            raise ValueError('El celular esta apagado')
        
    def __str__(self):
        return f'El celular de {self.nombre} modelo {self.modelo} tiene numero de celular {self.numero}'

    #METODO SINCRONIZACION
    
#DUDAS LEANDRO: TORRE

#main
torre=Torre()
celu = Celular('Isidro', 'iphone 15', 'iOS 7.1', 150, 64, 1156789023)
try:
    celu.desbloquear()
except ValueError as e:
    print(e)

try:
    celu.apagar()
except ValueError as e:
    print(e)

try:
    celu.bloquear()
except ValueError as e:
    print(e)
    
celu.prender()
celu.desbloquear()
celu.activarInternet()
celu.activarRedMovil()

celu2 = Celular('Andres', 'iphone 15', 'iOS 7.1', 150, 64, 1167671659)
celu2.prender()
celu2.activarInternet()
celu2.activarRedMovil()

torre.agregarTelefono(celu)
torre.agregarTelefono(celu2)

celu2.aplicaciones['Contactos'].agregarContacto('isidro',1156789023)
celu.aplicaciones['Telefono'].llamar(1167671659,torre)
a=input('hola')
celu.aplicaciones['Telefono'].cortarLlamada(torre)
print(celu.aplicaciones['Telefono'].registroDeLlamadas)
print('')
print(celu2.aplicaciones['Telefono'].registroDeLlamadas)
print('')
print(torre.registroDeLlamadas)









# alicaciones={'Telefono': 'Telefono(self.numero)'}
# celu.abrirAplicacion('Telefono')
# #self.appActiva = Telefono()
# celu.salirAplicacion()      #self.appActiva = None  
# #self.appActiva = AppStore()  
# #self.appActiva = 

# #self.telefono=Telefono(self.numero)

