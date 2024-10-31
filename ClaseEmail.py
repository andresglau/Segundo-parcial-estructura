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
    def leerMail(self):
        self.leido = True
    def destacarMail(self):
        self.destacado = True
    def __str__(self):
        return f'Mail de {self.mailEmisor} a {self.mailReceptor} el {self.fecha}'
    def __repr__(self):
        return self.__str__()

class Email(Aplicacion):
    nombre = 'Email'
    icono = None
    emailsRegistrados = {}
    def __init__(self, miMail: str):
        if miMail in Email.emailsRegistrados:           #VALIDAR ADEMAS QUE SEA UN FORMATO DE MAIL VALIDO
            raise ValueError('No puede tener ese mail')
        self.miMail = miMail
        Email.emailsRegistrados[miMail]=self
        
        self.bandejaEntrada = deque()           #PILA
        self.bandejaEnviados = deque()          #PILA
        self.noLeidos = set()                   #almacena los mails no leidos y los marcados como no leidos
        self.destacados = set()                 #almacena los mails destacados

    def mandarMail(self, mailDestinatario):
        if mailDestinatario not in Email.emailsRegistrados:
            raise ValueError('Ese email no esta disponible')
        mail = Mail(self.miMail, mailDestinatario)
        self.bandejaEnviados.appendleft(mail)
        Email.emailsRegistrados[mailDestinatario].recibirMail(mail)

    def recibirMail(self, mail):
        self.bandejaEntrada.appendleft(mail)

    # def abrirMail(self, )
    
    def verBandejaEntrada(self):
        for indice, mail in enumerate(self.bandejaEntrada):
            print(indice,': ', mail)
    
    
# pila = deque()
# pila.appendleft('Ultimo')
# pila.appendleft('Anteultimo')
# pila.appendleft('Primero')
# pila.popleft()
# for i in pila:
#     print(i)