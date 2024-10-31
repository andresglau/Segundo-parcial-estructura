from ClaseAplicacion import Aplicacion
class AppStore(Aplicacion):
    nombre = 'App Store'
    icono = None
    aplicacionesDisponibles = {}
    #Diccionario {clave nombreAplicacion : valor clase} {Notas.nombre: Notas, Calendario.nombre:Calendario,Calculadora.nombre:Calculadora}
    def __init__(self, celular):
        self.celular=celular
    @classmethod
    def verAplicacionesDisponibles(cls):
        for aplicacion in cls.aplicacionesDisponibles:
            print(aplicacion)

    def descargarAplicacion(self, nombre):
        if nombre not in self.aplicacionesDisponibles:
            print(f'{nombre} no se encuentra en el App Store') #no levanta error ya que es una situacion comun que se puede dar
        else:
            if nombre in self.celular.aplicaciones:
                print(f'{nombre} ya esta descargada en el celular')
            else:
                self.celular.aplicaciones[nombre]=self.aplicacionesDisponibles[nombre]() #creemos que no es necesario hacer un metodo en celular para esto
                print(f'{nombre} se descargo en el celular')
