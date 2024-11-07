from ClaseAplicacion import Aplicacion
from ClaseNota import Nota

class Notas(Aplicacion):
    nombre='Notas'
    icono=None
    
    def __init__(self):
        super.__init__()
        self.misNotas={}                #diccionario {titulo: objeto Nota}
        
        
    def crearNota(self,titulo):
        if titulo in self.misNotas:
            raise ValueError('Ya existe una nota con este título.')
        else:
            mensaje=input('Escriba la nota... ')
            nota=Nota(titulo,mensaje)
            self.misNotas[titulo]=nota
            
    def eliminarNota(self,titulo):
        if titulo not in self.misNotas:
            raise ValueError('La nota que deseas eliminar no existe.')
        else:
            del self.misNotas[titulo]
    
    def verNotas(self):
        for nota in list(sorted(self.misNotas.values(), reverse = True)):
            print(nota)
            
            
            