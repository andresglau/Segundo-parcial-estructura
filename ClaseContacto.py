class Contacto:
    def __init__(self,nombre, numTelefono):
        self.nombre=nombre
        self.numTelefono=numTelefono
        
    def cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        
    def cambiarNumTelefono(self,nuevoNumTelefono):
        self.numTelefono = nuevoNumTelefono
    
    def __lt__(self, other):
        if isinstance(other, Contacto):
            return self.nombre<other.nombre
        else:
            raise ValueError('No se puede comparar un contacto con otro objeto')
    
    def __str__(self):
        return f'\t Nombre: {self.nombre} \t Numero de telefono: {self.numTelefono}'
    
    def __repr__(self):
        return self.__str__()