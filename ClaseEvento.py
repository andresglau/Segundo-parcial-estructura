class Evento:
    def __init__(self, evento, fecha): 
        self.evento=evento
        self.fecha=fecha
        
    def cambiarFecha(self, fechaNueva):
        self.fecha=fechaNueva
        
    def cambiarEvento(self, eventoNuevo):
        self.evento=eventoNuevo
        
    def __lt__(self, other):
        return self.fecha<other.fecha
        
    def __str__(self):
        return f'Evento: {self.evento}, Fecha: {self.fecha} '
    
    def __repr__(self):
        return self.__str__()