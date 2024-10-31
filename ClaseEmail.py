from ClaseAplicacion import Aplicacion
from collections import deque
from datetime import datetime, date

class Mail():
    def __init__(self, mailEmisor, mailReceptor, asunto: str, contenido: str):        
        self.mailEmisor = mailEmisor
        self.mailReceptor = mailReceptor
        self.asunto = asunto
        self.contenido = contenido
        self.fecha = date.today()
    def __str__(self):
        return f'Mail de {self.mailEmisor} a {self.mailReceptor} el {self.fecha}\nasunto: {self.asunto}'
    def __repr__(self):
        return self.__str__()

class Email(Aplicacion):
    nombre = 'Email'
    icono = None
    emailsRegistrados = {}
    def __init__(self, miMail: str):
        self.miMail = miMail
        self.emailsRegistrados[miMail]=self     #al instanciar el telefono se verifica que no haya otro mail igual
        self.bandejaEntrada = deque()           #PILA
        self.bandejaEnviados = deque()          #PILA
        self.noLeidos = set()                   #almacena los mails no leidos y los marcados como no leidos
        self.destacados = set()                 #almacena los mails destacados

    def mandarMail(self, mailDestinatario):
        if mailDestinatario not in self.emailsRegistrados:
            raise ValueError('Ese email no esta disponible')
        mail = Mail(self.miMail, mailDestinatario)
        self.bandejaEnviados.appendleft(mail)
        self.emailsRegistrados[mailDestinatario].recibirMail(mail)

    def recibirMail(self, mail):
        self.bandejaEntrada.appendleft(mail)
        self.noLeidos.add(mail)
    
    def verBandejaEntrada(self):
        for indice, mail in enumerate(self.bandejaEntrada):
            print(indice,': ', mail, sep='')
            
    def verBandejaEntradaPorNoLeido(self):
        noLeidos=''
        leidos=''
        for indice, mail in enumerate(self.bandejaEntrada):
            if mail in self.noLeidos:
                noLeidos+=str(indice)+': '+str(mail)+'\n'
            else:
                leidos+=str(indice)+': '+str(mail)+'\n'
        print(f'Mails no leidos:\n{noLeidos}Mails leidos:\n{leidos}')
        
    def abrirMail(self, pos):
        if not self.bandejaVacia():
            if pos in range(0,len(self.bandejaEntrada)):
                print(self.bandejaEntrada[pos],self.bandejaEntrada[pos].contenido,sep='\n')
            else:
                print('Posicion fuera de rango')
        
    def marcarComoNoLeido(self, pos):
        if not self.bandejaVacia():
            if pos in range(0,len(self.bandejaEntrada)):
                self.noLeidos.add(self.bandejaEntrada[pos]) #si ya estaba como no leido no pasa nada
            else:
                print('Posicion fuera de rango')
                
    def destacar(self, pos): #falta el contrario. ver si dejamos destacar o no. para mi al pedo
        if not self.bandejaVacia():
            if pos in range(0,len(self.bandejaEntrada)):
                self.destacados.add(self.bandejaEntrada[pos]) #si ya estaba destacado no pasa nada
            else:
                print('Posicion fuera de rango')
                
    def eliminar(self, pos): #solamente lo elimina de mi bandeja de entrada
        if not self.bandejaVacia():
            if pos in range(0,len(self.bandejaEntrada)):
                pass #como se elimina en un deque por posicion?
            else:
                print('Posicion fuera de rango')
                
    def bandejaVacia(self):
        if self.bandejaEntrada:
            return False
        print('Bandeja de entrada vacia')
        return True
    
pila = deque()
pila.appendleft('Primero')
pila.appendleft('Segundo')
pila.appendleft('Ultimo')
for i,clave in enumerate(pila):
    print(i,': ', clave, sep='')
    
print(pila[0])