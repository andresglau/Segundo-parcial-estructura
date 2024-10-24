class Contacto:
    def __init__(self,nombre, numTelefono):
        self.nombre=nombre
        self.numTelefono=numTelefono
        
    def cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        
    def cambiarNumTelefono(self,nuevoNumTelefono):
        self.numTelefono = nuevoNumTelefono