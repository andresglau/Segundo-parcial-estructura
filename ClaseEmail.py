from ClaseAplicacion import Aplicacion
from collections import deque
from datetime import date

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

    def mandarMail(self, mailDestinatario,asunto,contenido):
        if mailDestinatario not in self.emailsRegistrados:
            raise ValueError('Ese email no esta disponible')
        mail = Mail(self.miMail, mailDestinatario,asunto,contenido)
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
                self.noLeidos.discard(self.bandejaEntrada[pos]) #marca como leido el mail. Si ya esta leido, no tira error.
            else:
                print('Posicion fuera de rango')
        
    def marcarComoNoLeido(self, pos):
        if not self.bandejaVacia():
            if pos in range(0,len(self.bandejaEntrada)):
                self.noLeidos.add(self.bandejaEntrada[pos]) #si ya estaba como no leido no pasa nada
            else:
                print('Posicion fuera de rango')
                
    def eliminar(self, pos): #solamente lo elimina de mi bandeja de entrada. De los enviados asumimos que no se puede borrar.
        if not self.bandejaVacia():
            if pos in range(0,len(self.bandejaEntrada)):
                del self.bandejaEntrada[pos]
            else:
                print('Posicion fuera de rango')
                
    def verBandejaEnviado(self):
        for indice, mail in enumerate(self.bandejaEnviados):
            print(indice,': ', mail, sep='')
        
    def abrirMailEnviado(self, pos):
        if self.bandejaEnviados:
            if pos in range(0,len(self.bandejaEnviados)):
                print(self.bandejaEnviados[pos],self.bandejaEnviados[pos].contenido,sep='\n')
            else:
                print('Posicion fuera de rango')
        else:
            print('Bandeja de enviados vacia')
                
    def bandejaVacia(self):
        if self.bandejaEntrada:
            return False
        print('Bandeja de entrada vacia')
        return True
    
# ichi=Email('isidro@gmail.com')
# andi=Email('andres@gmail.com')
# fede=Email('fede@gmail.com')
# manu=Email('manu@gmail.com')

# ichi.mandarMail(andi.miMail,'saludo','hola como estas')
# fede.mandarMail(andi.miMail,'boca','gano boca')
# manu.mandarMail(andi.miMail,'river','gano river')
# ichi.mandarMail(andi.miMail,'tp','cuando hacemos el tp')
# ichi.mandarMail(andi.miMail,'chau','nos vemos')

# # andi.verBandejaEntrada()
# # ichi.verBandejaEnviado()
# # ichi.abrirMailEnviado(2)
# andi.abrirMail(1)
# andi.abrirMail(3)
# print()
# andi.verBandejaEntrada()
# print()
# andi.verBandejaEntradaPorNoLeido()