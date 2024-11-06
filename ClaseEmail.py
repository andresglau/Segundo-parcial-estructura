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
        super().__init__()
        self.miMail = miMail
        self.emailsRegistrados[miMail]=self     #al instanciar el telefono se verifica que no haya otro mail igual
        self.bandejaEntrada = deque()           #PILA
        self.bandejaEnviados = deque()          #PILA
        self.noLeidos = set()                   #almacena los mails no leidos y los marcados como no leidos
        self.opciones = [('Redactar un mail',self.mandarMail,[]),
                        ('Abrir mail', self.abrirMail, []),
                        ('Ver bandeja de entrada (por fecha)', self.verBandejaEntrada,[]),
                        ('Ver bandeja de entrada (por no leidos)', self.verBandejaEntradaPorNoLeido,[]),
                        ('Marcar como no leido',self.marcarComoNoLeido,[]),
                        ('Eliminar mail',self.eliminar,[]),
                        ('Ver bandeja de enviados',self.verBandejaEnviado,[]),
                        ('Abrir mail enviado',self.abrirMailEnviado,[]),
                        ('Volver a pantalla de inicio', self.volver, [])]

    def mandarMail(self):
        mailDestinatario=input('Ingrese el mail del destinatario: ')
        if mailDestinatario not in self.emailsRegistrados:
            print('Ese email no esta disponible')
        else:
            asunto=input('Ingrese el asunto: ')
            contenido=input('Ingrese el contenido: ')
            mail = Mail(self.miMail, mailDestinatario,asunto,contenido)
            self.bandejaEnviados.appendleft(mail)
            self.emailsRegistrados[mailDestinatario].recibirMail(mail)

    def recibirMail(self, mail):
        self.bandejaEntrada.appendleft(mail)
        self.noLeidos.add(mail)
    
    def verBandejaEntrada(self):
        print('Bandeja de mails recibidos:')
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
        
    def abrirMail(self):
        pos = input('Ingrese la posicion del mail en la bandeja de entrada: ')
        if not pos.isdigit():
            print('Invalido: No ingreso una posicion')
        else:
            pos = int(pos)
            if not self.bandejaVacia():
                if pos in range(0,len(self.bandejaEntrada)):
                    print(self.bandejaEntrada[pos],self.bandejaEntrada[pos].contenido,sep='\n')
                    self.noLeidos.discard(self.bandejaEntrada[pos]) #marca como leido el mail. Si ya esta leido, no tira error.
                else:
                    print('Posicion fuera de rango')
            else:
                print('No hay mails en la bandeja')
        
    def marcarComoNoLeido(self):
        pos = input('Ingrese la posicion del mail a marcar como no leido en la bandeja de entrada: ')
        if not pos.isdigit():
            print('Invalido: No ingreso una posicion')
        else:
            pos=int(pos)
            if not self.bandejaVacia():
                if pos in range(0,len(self.bandejaEntrada)):
                    self.noLeidos.add(self.bandejaEntrada[pos]) #si ya estaba como no leido no pasa nada
                else:
                    print('Posicion fuera de rango')
            else:
                print('No hay mails en la bandeja')
                
    def eliminar(self): #solamente lo elimina de mi bandeja de entrada. De los enviados asumimos que no se puede borrar.
        pos = input('Ingrese la posicion del mail a eliminar en la bandeja de entrada: ')
        if not pos.isdigit():
            print('Invalido: No ingreso una posicion')
        else:
            pos=int(pos)
            if not self.bandejaVacia():
                if pos in range(0,len(self.bandejaEntrada)):
                    del self.bandejaEntrada[pos]
                    print(f'Se elimino: {self.bandejaEntrada[pos]}')
                else:
                    print('Posicion fuera de rango')
            else:
                print('No hay mails en la bandeja')
                
    def verBandejaEnviado(self):
        print('Bandeja de enviados:')
        for indice, mail in enumerate(self.bandejaEnviados):
            print(indice,': ', mail, sep='')
        
    def abrirMailEnviado(self):
        pos = input('Ingrese la posicion del mail enviado en la bandeja de enviados: ')
        if not pos.isdigit():
            print('Invalido: No ingreso una posicion')
        else:
            pos=int(pos)
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