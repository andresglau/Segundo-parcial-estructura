import datetime
class Evento:
    def __init__(self, evento, fecha: datetime.date): 
        self.evento=evento
        self.fecha=fecha
        
    def cambiarFecha(self, fechaNueva):
        '''
        Cambia la fecha
        '''
        self.fecha=fechaNueva
        
    def cambiarEvento(self, eventoNuevo):
        '''
        Cambia el nombre del evento
        '''
        self.evento=eventoNuevo
        
    def __lt__(self, other):
        return self.fecha<other.fecha
        
    def __str__(self):
        return f'Evento: {self.evento}, Fecha: {self.fecha} '
    
    def __repr__(self):
        return self.__str__()