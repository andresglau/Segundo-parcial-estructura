from ClaseAplicacion import Aplicacion
from ClaseNota import Nota

class Notas(Aplicacion):
    nombre='Notas'
    icono=None
    
    def __init__(self,misNotas):
        super.__init__()
        self.misNotas={}                #diccionario {titulo: objeto Nota}
        
        
        def crearNota(self,titulo):
            if titulo in self.misNotas:
                raise ValueError('Ya existe una nota con este título.')
            else:
                mensaje=input('Que quieres decir?')
                nota=Nota(titulo,mensaje)
                self.misNotas[titulo]=nota
                
        def eliminarNota(self,titulo):
            if titulo not in self.misNotas:
                raise ValueError('La nota que deseas eliminar no existe.')
            else:
                del self.misNotas[titulo]
        
        def verNotas(self):
            print 
                
                
                