from ClaseAplicacion import Aplicacion

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
                pass