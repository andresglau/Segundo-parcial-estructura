from collections import deque
from ClaseAplicacion import Aplicacion

class Contacto:
    def __init__(self, nombre, numTelefono=None, correo=None):
        self.nombre = nombre
        self.numTelefono = numTelefono
        self.correo = correo

class Telefono(Aplicacion):
    nombre = 'Telefono'
    icono = None
    
    def __init__(self, miNumero):
        self.miNumero = miNumero
        self.contactos = {}
        self.registroLlamadas = deque()     #cola. FIFO. appendleft
        
        
        
        
        
# class SMS(Aplicacion):
#     def __init__(self):
#         self.contactosMensajes={}
#         self.casillaMensajes=deque()
        