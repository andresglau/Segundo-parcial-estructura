from ClaseAplicacion import Aplicacion
from ClaseEvento import Evento
import datetime

class Calendario(Aplicacion):
    nombre = 'Calendario'
    icono = 'FotosApps/FotoAppCalendario.jpg'
    
    def __init__(self):
        super().__init__()
        self.eventos={}         #{nombre del evento : objeto Evento}
        self.opciones=[('Crear evento',self.crearEvento,[]),
                       ('Eliminar evento',self.eliminarEvento,[]),
                       ('Ver eventos de una fecha',self.verEventosPorFecha,[]),
                       ('Ver eventos pendientes',self.verEventosPendientes,[]),
                       ('Cambiar evento',self.cambiarEvento,[]),
                       ('Cambiar fecha de un evento',self.cambiarFechaEvento,[]),
                       ('Volver a pantalla de inicio', self.volver, [])]
    
    def pedirYConvertirFecha(self):
        '''
        Devuelve una fecha ingresada por el usuario mediante un objeto datetime.date
        '''
        while True:
            try:
                dia=int(input('Ingrese el dia: '))
                mes=int(input('Ingrese el mes: '))
                anio=int(input('Ingrese el anio: '))
            except ValueError:
                print('Debe ingresar un numero entero')
            else:
                try:
                    return datetime.date(anio,mes,dia)
                except ValueError:
                    print('Debe ingresar una fecha valida')
    
    def crearEvento(self):
        '''
        Crea un evento nuevo. Pide el nombre del evento y la fecha del mismo.
        '''
        fecha=self.pedirYConvertirFecha()
        evento=input('Ingrese el evento: ')
        if evento in self.eventos:
            print('No podes tener 2 eventos con el mismo nombre: ') #aunque en la realidad no suceda, sino no podemos acceder a un objeto Evento
        else:
            self.eventos[evento]=(Evento(evento,fecha))
            
    def eliminarEvento(self):
        '''
        Elimina un evento segun el nombre con el que fue registrado.
        '''
        evento=input('Ingrese el evento: ')
        if evento not in self.eventos:
            print('No existe ese evento')
        else:
            print('Se elimino',self.eventos[evento])
            self.eventos.pop(evento)
            
    def verEventosPorFecha(self):
        '''
        Pide una fecha y muestra los eventos registrados en esa fecha.
        Muestra los eventos del mas antiguo al mas nuevo
        '''
        fecha=self.pedirYConvertirFecha()
        print('Eventos el',fecha)
        for evento in list(sorted(self.eventos.values())):
            if evento.fecha==fecha:
                print(evento)

    def verEventosPendientes(self):
        '''
        Muestra los eventos aun pendientes.
        Los imprime del mas antiguo al mas nuevo
        '''
        print('Eventos pendientes')
        for evento in list(sorted(self.eventos.values())):
            if evento.fecha>=datetime.date.today():
                print(evento)
                
    def cambiarFechaEvento(self):
        '''
        Cambia la fecha de un evento registrado
        '''
        evento=input('Ingrese el evento: ')
        if evento not in self.eventos:
            print('No existe ese evento')
        else:
            fecha=self.pedirYConvertirFecha()
            self.eventos[evento].cambiarFecha(fecha)
            
    def cambiarEvento(self):
        '''
        Cambia el nombre de un evento registrado.
        '''
        evento=input('Ingrese el evento que desea cambiar: ')
        if evento not in self.eventos:
            print('No existe ese evento')
        else:
            eventoNuevo=input('Ingresa un nuevo evento: ')
            self.eventos[eventoNuevo]=Evento(eventoNuevo,self.eventos[evento].fecha)
            self.eventos.pop(evento)