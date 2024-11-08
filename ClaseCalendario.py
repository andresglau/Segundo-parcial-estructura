from ClaseAplicacion import Aplicacion
from ClaseEvento import Evento

class Calendario(Aplicacion):
    def __init__(self):
        super().__init__()
        self.eventos={}
        
    def crearEvento(self):
        fecha=input('Ingresa una fecha: ') #ver si fecha se puede manejar como datetime
        evento=input('Ingrese el evento: ')
        if evento in self.eventos:
            print('No podes tener 2 eventos con el mismo nombre: ') #aunque en la realidad no suceda, sino no podemos acceder a un objeto evento
        else:
            self.eventos[evento]=(Evento(evento,fecha))
            
    def eliminarEvento(self):
        evento=input('Ingrese el evento: ')
        if evento not in self.eventos:
            print('No existe ese evento')
        else:
            print('Se elimino',self.eventos[evento])
            self.eventos.pop(evento)
            
    def verEventosPorFecha(self):
        fecha=input('Ingresa una fecha: ')
        print('Eventos el',fecha)
        for evento in list(sorted(self.eventos, reverse = True)): #ver si usar el reverse o no
            if evento.fecha==fecha:
                print(evento)

    def verEventosPendientes(self):
        print('Eventos pendientes')
        for evento in list(sorted(self.eventos, reverse = True)): #ver si usar el reverse o no
            if evento.fecha>='08/11': #corregir con datetime
                print(evento)
                
    def cambiarFechaEvento(self):
        evento=input('Ingrese el evento: ')
        if evento not in self.eventos:
            print('No existe ese evento')
        else:
            fecha=input('Ingresa una fecha: ')
            self.eventos[evento].cambiarFecha(fecha)
            
    def cambiarEvento(self):
        evento=input('Ingrese el evento que desea cambiar: ')
        if evento not in self.eventos:
            print('No existe ese evento')
        else:
            eventoNuevo=input('Ingresa un nuevo evento: ')
            self.eventos[eventoNuevo]=Evento(eventoNuevo,self.eventos[evento].fecha)
            self.eventos.pop(evento)
           