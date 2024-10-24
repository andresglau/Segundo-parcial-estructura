from collections import deque
from ClaseContacto import Contacto

class Contacto:
    def __init__(self, nombre, numTelefono = None):
        self.nombre = nombre
        self.numTelefono = numTelefono

class Aplicacion():
    aplicacionesDisponibles={}
    nombre = ''
    icono = None
    def __init__(self):
        pass

class AplicacionComunicacion(Aplicacion):       #ACA SE INCLUYE A TELEFONO, CONTACTOS (hay que ver SMS pero me parece que no)
    def __init__(self):
        super().__init__()
        self.contactos = {}
    #agregar contacto. no hace falta verificar que exista ya que es lo que uno tiene agendado       #NO HAY REPETIDOS, ACLARAR
    def agregarContacto(self, nombre, numTelefono = None):
        self.contactos.update({(nombre, numTelefono): Contacto(nombre, numTelefono)})
    def actualizarContacto(self, nombre, numTelefono = None, nuevoNom = None, nuevoNum = None):
        if not (nuevoNom or nuevoNum):
            print('Debe pasar un atributo para poder modificar el contacto')
        # self.contactos.update({nombre, None}: )
    
    def busco_contactos(self, nombre, numTelefono = None):
        if nombre and numTelefono:
            return list(filter(lambda x: (nombre, numTelefono) in x, self.contactos))
        return list(filter(lambda x: (nombre, None) in x, self.contactos))

    #         self.contactos.update
            
    #eliminar contacto
    # def eliminarContacto(self, nombre):
    #     if nombre not in self.contactos:
    #         raise ValueError('No existe este contacto')
    #     else:
    #         self.contactos.pop(nombre)
    def verContactos(self):
        for elem in self.contactos:
            nom = elem.items()
            print(f'{nom} // ')
        
app = AplicacionComunicacion()
app.agregarContacto('Isidro', 1234567)
app.agregarContacto('Isidro', 1234567)
print(app.contactos)
# app.verContactos()

class Telefono(AplicacionComunicacion):
    nombre = 'Telefono'
    icono = None        #DEFINIR
    def __init__(self, miNumero):
        super().__init__()
        self.miNumero = miNumero
        self.registroLlamadas = deque()     #cola. FIFO. appendleft

#################################################################################################

    
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
        
        
        
        
# class SMS(Aplicacion):
#     def __init__(self):
#         self.contactosMensajes={}
#         self.casillaMensajes=deque()
        
dic={'andi':Contacto('andi',1)}
print(list(map(lambda contacto: contacto.numTelefono,dic.values())))