class Celular:
    
    idUnicos=set()
    modelosPermitidos={'iphone 15','iphone 16','samsung s20'}
    
    def __init__(self, nombre: str, modelo: str, version: str, memoriaRAM: int, almacenamiento: int, numero: int):
        #verificaciones
        if modelo not in self.modelosPermitidos:
            raise ValueError('modelo no permitido')
        if len(str(numero))!=10 or str(numero)[:2]!='11' or str(numero)[2]=='0' or numero<0:
            raise ValueError('numero de celular incorrecto. Debe tener el siguiente formato: 1123456789')
        #instanciar
        if self.idUnicos:
            self.id=max(self.ids)+1
        else:
            self.id=1000
        self.idUnicos.add(self.id)
        self.nombre=nombre
        self.modelo=modelo
        self.version = version
        self.memoriaRAM = memoriaRAM
        self.almacenamiento=almacenamiento
        self.numero=numero
        
        self.apagado = True
        self.bloqueado = True
        
    def prender(self):
        if self.apagado:
            self.apagado = False
            print('Se prendio el celular')
        else:    
            raise ValueError('El celular ya esta prendido')
    def apagar(self):
        if not self.apagado:
            if not self.bloqueado:
                self.bloquear()
            self.apagado = True
            print('Se apago el celular')
        else:
            raise ValueError('El celular ya esta apagado')
    def desbloquear(self):
        if not self.apagado:
            if self.bloqueado:
                self.bloqueado = False
                print('Se desbloqueo el celular')
            else:
                raise ValueError('El telefono ya esta desbloqueado')
        else:
            raise ValueError('El celular esta apagado. Debe prenderlo para desbloquear')
            
    def bloquear(self):
        if not self.apagado:
            if not self.bloqueado:
                self.bloqueado = True
                print('Se bloqueo el celular')
            else:
                raise ValueError('El telefono ya esta bloqueado')
        else:
            raise ValueError('El celular esta apagado. Debe prenderlo para desbloquear')
    def __str__(self):
        return f'El celular de {self.nombre} modelo {self.modelo} tiene numero de celular {self.numero}'
#llegamos hasta el segundo metodo


#main
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
celu.apagar()
