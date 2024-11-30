from ClaseAplicacion import Aplicacion
from ClaseNota import Nota

class Notas(Aplicacion):
    nombre='Notas'
    icono='FotosApps/FotoAppNotas.jpg'
    
    def __init__(self):
        super().__init__()
        self.misNotas={}               #diccionario {titulo: objeto Nota}
        self.notaAbierta = False
        self.opciones=[
                         ('Crear una nota nueva',self.crearNota,[]),
                         ('Abrir una nota',self.abrirNota,[]),
                         ('Ver las notas',self.verNotas,[]),
                         ('Borrar una nota',self.eliminarNota,[]),
                         ('Cerrar nota',self.cerrarNota,[]),
                         ('Sobreescribir nota abierta',self.sobreescribirNotaAbierta,[]),
                         ('Agregar contenido nota abierta', self.agregarContenidoNotaAbierta,[]),
                         ('Ver nota abierta',self.verNotaAbierta,[]),
                         ('Volver a pantalla de inicio', self.volver, [])]
        
    def crearNota(self):
        '''
        Se crea una nota si es que el titulo no existe
        '''
        try:
            titulo=input('Ingrese el titulo: ')
            if titulo in self.misNotas:
                raise ValueError('Ya existe una nota con este título')
            else:
                contenido=input('Escriba el contenido de la nota: ')
                nota=Nota(titulo,contenido)
                self.misNotas[titulo]=nota
                print('Nota creada')
        except ValueError as e:
            print(e)
    
    def abrirNota(self):
        '''
        Abre una nota ya creada que permite distintas
        funcionalidades sobre esta
        '''
        if self.notaAbierta==False:
            try:
                titulo=input('Ingrese el titulo: ')
                if titulo not in self.misNotas:
                    raise ValueError('No existe una nota con este título')
            except ValueError as e:
                print(e)
            else:
                self.notaAbierta = self.misNotas[titulo]
                print('Se abrio la nota')
        else:
            print('Ya hay una nota abierta')
            
    def cerrarNota(self):
        '''
        Cierra una nota abierta
        '''
        if self.notaAbierta==False:
            print('No hay una nota abierta')
        else:
            self.notaAbierta = False
            print('Se cerro la nota')
    
    def eliminarNota(self):
        '''
        Elimina una nota
        '''
        titulo=input('Ingrese el titulo: ')
        try:
            if titulo not in self.misNotas:
                raise ValueError('La nota que deseas eliminar no existe.')
            elif titulo==self.notaAbierta.titulo:
                print('No puede eliminar la nota abierta')
            else:
                print(self.misNotas[titulo],'eliminada')
                self.misNotas.pop(titulo)
        except ValueError as e:
            print(e)
    
    def verNotas(self):
        '''
        Muestra las notas ordenadas de mas reciente a mas 
        antigua en funcion de la ultima modificacion
        '''
        if self.misNotas:
            for nota in list(sorted(self.misNotas.values(), reverse = True)):
                print(nota)
        else:
            print('No hay notas')
            
    def volver(self):
        '''
        Modifica el metodo volver predeterminado agregandole que
        cierre la nota que estaba abierta antes de salir
        '''
        self.cerrarNota()
        return True
            
    def sobreescribirNotaAbierta(self):
        '''
        Sobreescribe la nota abierta
        '''
        if not self.notaAbierta:
            print('No hay ninguna nota abierta')
        else:
            self.notaAbierta.sobreescribirNota()
            
    def agregarContenidoNotaAbierta(self):
        '''
        Agrega contenido a la nota abierta
        '''
        if not self.notaAbierta:
            print('No hay ninguna nota abierta')
        else:
            self.notaAbierta.agregarContenido()
        
    def verNotaAbierta(self):
        '''
        Muestra el contenido de la nota abierta
        '''
        if not self.notaAbierta:
            print('No hay ninguna nota abierta')
        else:
            self.notaAbierta.verNota()