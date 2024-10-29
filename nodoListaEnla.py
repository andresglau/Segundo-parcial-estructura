class Nodo:
    def __init__(self,dato:int):
        self.dato = dato
        self.siguiente = None
        
    def __str__(self):
        return f'almaceno {self.dato}'