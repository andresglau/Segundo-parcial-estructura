from exportadorCSV import *
import Validaciones
from ClaseTorre import Torre
from ClaseEmail import Email
from ClaseCelular import Celular
import pickle

#metodos comunes de menu
def mostrarMenu(lista):
    '''
    A partir de la lista de tuplas muestra enumerada la lista de opciones,
    Luego valida la opcion. Y por ultimo la ejecuta
    '''
    print()
    nuevaLista=list(map(lambda tupla: tupla[0],lista))
    for i, opcion in enumerate(nuevaLista):
        print(i,opcion)
    opcion=input('Ingrese la opcion: ')
    while not validarOpcion(opcion, lista):
        opcion=input('Ingrese la opcion: ')
    if ejecutarOpcion(opcion,lista)==True:
        return True

def validarOpcion(opcion,lista):
    '''
    Valida la opcion elegida en mostrar menu
    '''
    try:
        opcion=int(opcion)
    except ValueError:
        print('No ingresaste un numero')
    else:
        if opcion in range(0,len(lista)):
            return True
        print('Opcion invalida. Fuera del rango')
    return False
     
def ejecutarOpcion(opcion,lista):
    '''
    Ejecuta la opcion seleccionada. Se llama a la funcion sin parantesis,
    y se le agrega el parentesis con un spread dentro que se transforman 
    en los parametros
    '''
    return lista[int(opcion)][1](*lista[int(opcion)][2])

def mostrarOpciones(lista):
    '''
    A diferencia de mostrarMenu, esta funcion no ejecuta la opcion sino que la devuelve.*args
    Sirve para la funcion de instanciacion de celulares
    '''
    for i, opcion in enumerate(lista):
        print(i,opcion)
    opcion=input('Ingrese la opcion: ')
    while not validarOpcion(opcion, lista):
        opcion=input('Ingrese la opcion: ')
    return int(opcion)

#funciones especificas
def terminar():
    '''
    Muestra programa terminado y se termina de mostrar el menu
    '''
    print("Programa terminado")
    
#FuncionInstanciar
def instanciar(torre: Torre, menuOperar):
    '''
    Pide todos los datos necesarios para instanciar un celular, los valida
    y hasta que no sean correctos los vuelve a pedir. Una vez todos validados,
    muestra el menu base de nuevo
    '''
    Celular(pedirNombre(), pedirModelo(),pedirVersion(),pedirMemoriaRAM(),pedirAlmacenamientoGB(),pedirNumero(), pedirCodigo(), pedirMail(),torre)
    mostrarMenu([('Instanciar',instanciar,[torre]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    
def pedirNombre():
    nombre = input('Ingrese un nombre para el celular: ')
    return nombre
def pedirModelo():
    print('Ingrese el modelo del celular')
    listaModelosPermitidos=['iphone 15','iphone 16','samsung s20']
    return listaModelosPermitidos[mostrarOpciones(listaModelosPermitidos)]
def pedirVersion():
    print('Ingrese la version del celular')
    listaVersionesPermitidas = ['version 1', 'version 2', 'version 3', 'version 4']
    return listaVersionesPermitidas[mostrarOpciones(listaVersionesPermitidas)]
def pedirMemoriaRAM():
    print('Ingrese la memoria RAM del celular')
    memoriasPermitidas=[4,8,16,32]
    return memoriasPermitidas[mostrarOpciones(memoriasPermitidas)]
def pedirAlmacenamientoGB():
    print('Ingrese el almacenamiento del celular')
    listaAlmacenamientosDisponibles = [32, 64, 128, 256]
    return listaAlmacenamientosDisponibles[mostrarOpciones(listaAlmacenamientosDisponibles)]
def pedirNumero():
    cumple=False
    while not cumple:
        numero=input('Ingrese el numero de celular: ')
        if Validaciones.validarFormatoNumTelefono(numero):
            pass
        elif int(numero) in Celular.numerosUso:
            print('Numero de celular usado')
        else:
            cumple=True
    return int(numero)
def pedirCodigo():
    cumple=False
    while not cumple:
        codigo=input('Ingrese el codigo de desbloqueo: ')
        if len(codigo)==4 and codigo.isdigit():
            cumple=True
        else:
            print('codigo de desbloqueo incorrecto. Debe tener el siguiente formato: 1234')
    return int(codigo)
def pedirMail():
    valido = False
    while not valido:
        mail = input('Ingrese un mail para registrar en el celular:')
        if mail in Email.emailsRegistrados:
            print('No puede tener ese mail. Ya lo tiene otro usuario')
        elif '@' not in mail or '.com' not in mail[-4:]:      #Esta es nuestra humilde validacion de mail
            print('Formato de mail no valido')
        else:
            valido = True
    return mail

#funcion operar
def operar(menuOperar):
    '''
    Pide un numero de celular para operarlo y lo define como el celular activo
    o se ingresa 1 para volver al menu base
    '''
    existe=False
    while not existe:
        try:
            print('Numeros de telefono para operar: ')
            for numero in Celular.numerosUso:
                print('\t',numero)
            opcion=int(input('Ingrese un numero de telefono. Ingrese 1 para volver atras: '))
            if opcion==1 or opcion in Celular.numerosUso:
                existe=opcion
            else:
                print('Numero de telefono inexistente')
        except ValueError:
            print('Debe ingresar una opcion valida')
    if existe==1:
        mostrarMenu([('Instanciar',instanciar,[torre]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    else:
        global celularActivo #definimos esta variable global para no estar todo el tiempo pasando el celular activo como parametro
        celularActivo=Celular.numerosUso[existe]
        mostrarMenu(menuOperar)
        
def salir():
    '''
    Este metodo vuelve al menu base desde cualquier otro menu.
    Si el celular no estaba bloqueado lo bloquea.
    '''
    if not celularActivo.bloqueado: 
        celularActivo.bloquear()
    mostrarMenu([('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    
def prender(menuPrender):
    '''
    Prende un celular y si ya estaba prendido no hace nada.
    Muestra el menu prender
    '''
    if celularActivo.apagado:
        celularActivo.prender()
    mostrarMenu(menuPrender)
    
#funciones prender
def apagar():
    '''
    Apaga el celular.
    Muestra el menu operar
    '''
    celularActivo.apagar()
    mostrarMenu([('Prender', prender,[menuPrender]), ('Salir', salir,[])])
    
def desbloquear(menuDesbloquear):
    '''
    Pide el codigo de desbloqueo e intenta desbloquearlo.
    Si falla 6 veces se vuelve al menu base
    Si acierta se muestra el menu desbloquear
    '''
    i=0
    while celularActivo.bloqueado and i<6:
        celularActivo.desbloquear()
        i+=1
    if celularActivo.bloqueado:
        print('Agoto los 6 intentos de desbloqueo')
        mostrarMenu([('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    else:
        mostrarMenu(menuDesbloquear)
        
#funciones desbloquear
def bloquear():
    '''
    Bloquea el celular y muestra el menu prender
    '''
    celularActivo.bloquear()
    prender([('Desbloquear', desbloquear,[menuDesbloquear]), ('Apagar', apagar,[]), ('Salir', salir,[])])
    
def abrirApp():
    '''
    Muestra las aplicaciones que estan descargadas en el celular.
    Valida que la aplicacion este descargada.
    Verifica si tiene internet para las apps que lo necesitan.
    Muestra el menu de la aplicacion.
    Cuando sale del menu de la aplicacion muestra el menu desbloquear
    '''
    celularActivo.verAplicaciones()
    app=input('Ingrese el nombre de la aplicacion: ')
    if app in celularActivo.aplicaciones:
        if app in ('SMS', 'Email', 'App Store') and not celularActivo.internet:
            print(f'No se puede acceder a {app} sin internet')
        else:
            volver = False
            while not volver:
                volver = mostrarMenu(celularActivo.aplicaciones[app].opciones)
    else:
        print('Esa aplicacion no se encuentra en el celular')
    mostrarMenu([('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])])

def eliminarApp():
    '''
    Intenta eliminar la app. Independientemente de que la elimine o 
    por alguna razon no pueda eliminarla, luego muestra el menu desbloquear
    '''
    try:
        celularActivo.borrarAplicacion()
    except ValueError as e:
        print(e)
    finally:
        mostrarMenu([('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])])

#Main
try:
    with open('celularNumerosUso.pkl', 'rb') as archivo:
        Celular.numerosUso = pickle.load(archivo)

    with open('celularIdUnicos.pkl', 'rb') as archivo:
        Celular.idUnicos = pickle.load(archivo)
        
    with open('torre.pkl', 'rb') as archivo:
        torre = pickle.load(archivo)
    
    #actualiza la torre dentro de cada celular ya que apunta hacia la de la ejecucion previa 
    for celular in Celular.numerosUso.values():
        celular.aplicaciones['Telefono'].torre = torre
        celular.aplicaciones['SMS'].torre = torre
        celular.aplicaciones['Configuracion'].torre = torre
        
    #actualiza los objetos del diccionario para que apunten a la misma direccion
    torre.telefonosRegistrados=Celular.numerosUso
        
    # torre=Torre()
    menuDesbloquear = [('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])]
    menuPrender=[('Desbloquear', desbloquear,[menuDesbloquear]), ('Apagar', apagar,[]), ('Salir', salir,[])]
    menuOperar=[('Prender', prender,[menuPrender]), ('Salir', salir,[])]
    menuBase=[('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])]

    # archivo = 'MemoriaCelulares.csv'
    # lectorCSV(archivo, torre) #trae a todos los telefonos instanciados previamente

    # for celular in Celular.numerosUso.values(): #activa estos metodos a todos los celulares por practicidad
    #     celular.apagado=False
    #     celular.redMovil=True
    #     celular.internet=True
    

    try:
        mostrarMenu(menuBase) #se ejecuta el menu
    except BaseException as e:
        print(f'Error no esperado. Error: {e}')
    
    if isinstance(torre, Torre):
        print(torre.telefonosRegistrados)
        print(torre.registroDeLlamadas)
        print(torre.registroDeMensajes)
        print(torre.mensajesPendientes)
        
    # sobreescribirCSV(archivo)
    with open('celularNumerosUso.pkl', 'wb') as archivo:
        pickle.dump(Celular.numerosUso, archivo)
        
    with open('celularIdUnicos.pkl', 'wb') as archivo:
        pickle.dump(Celular.idUnicos, archivo)
        
    with open('torre.pkl', 'wb') as archivo:
        pickle.dump(torre, archivo)
    
except:
    print('Error grave. Comunicarse.')