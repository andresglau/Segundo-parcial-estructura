from ClaseAplicacion import Aplicacion
from ClaseNotas import Notas
from ClaseCalculadora import Calculadora

class AppStore(Aplicacion):
    nombre = 'App Store'
    icono = None
    aplicacionesDisponibles = {Notas.nombre: Notas, Calculadora.nombre:Calculadora}
    #Diccionario {clave nombreAplicacion : valor clase} {Calendario.nombre:Calendario}
    def __init__(self, celular):
        super().__init__()
        self.celular=celular
        self.opciones = [('Ver aplicaciones disponibles en el App Store',self.verAplicacionesDisponibles,[]),
                         ('Descargar aplicacion',self.descargarAplicacion,[]),
                         ('Volver a pantalla de inicio', self.volver, [])]
    @classmethod
    def verAplicacionesDisponibles(cls):
        print('Aplicaciones que se pueden descargar:')
        for aplicacion in cls.aplicacionesDisponibles:
            print(aplicacion)

    def descargarAplicacion(self):
        nombre=input('Ingrese el nombre de la aplicacion que desea descargar: ')
        if nombre not in self.aplicacionesDisponibles:
            print(f'{nombre} no se encuentra en el App Store') #no levanta error ya que es una situacion comun que se puede dar
        else:
            if nombre in self.celular.aplicaciones:
                print(f'{nombre} ya esta descargada en el celular')
            else:
                self.celular.aplicaciones[nombre]=self.aplicacionesDisponibles[nombre]() #creemos que no es necesario hacer un metodo en celular para esto
                print(f'{nombre} se descargo en el celular')
