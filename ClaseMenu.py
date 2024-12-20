from exportadorCSV import *
import Validaciones
from ClaseTorre import Torre
from ClaseEmail import Email
from ClaseCelular import *
import pickle
import matplotlib.pyplot as plt
import matplotlib.image as img

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
    print('\n¿Que objeto desea instanciar?')
    opcion=mostrarOpciones(['Celular','Celular antiguo','Tablet'])
    if opcion==0:
        Celular(pedirNombre(), pedirModelo(),pedirVersion(),pedirMemoriaRAM(),pedirAlmacenamientoGB(),pedirNumero(), pedirCodigo(), pedirMail(),torre)
    elif opcion==1:
        CelularAntiguo(pedirNombre(), pedirModeloAntiguo(),pedirVersion(),pedirMemoriaRAM(),pedirAlmacenamientoGBAntiguo(),pedirNumero(), torre)
    else:
        Tablet(pedirNombre(), pedirModeloTablet(), pedirVersion(), pedirMemoriaRAM(), pedirAlmacenamientoGB(), pedirCodigo(), pedirMail())
    mostrarMenu([('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    
def pedirNombre():
    nombre = input('Ingrese un nombre para el dispositivo: ')
    return nombre
def pedirModelo():
    print('Ingrese el modelo del celular')
    listaModelosPermitidos=['iphone 15','iphone 16','samsung s20']
    return listaModelosPermitidos[mostrarOpciones(listaModelosPermitidos)]
def pedirModeloAntiguo():
    print('Ingrese el modelo del celular')
    listaModelosPermitidos=['nokia pluma','blackberry','LG']
    return listaModelosPermitidos[mostrarOpciones(listaModelosPermitidos)]
def pedirModeloTablet():
    print('Ingrese el modelo de la tablet')
    listaModelosPermitidos=['iPad5','TabletLG','Samsung Tablet']
    return listaModelosPermitidos[mostrarOpciones(listaModelosPermitidos)]
def pedirVersion():
    print('Ingrese la version del dispositivo')
    listaVersionesPermitidas = ['version 1', 'version 2', 'version 3', 'version 4']
    return listaVersionesPermitidas[mostrarOpciones(listaVersionesPermitidas)]
def pedirMemoriaRAM():
    print('Ingrese la memoria RAM del dispositivo')
    memoriasPermitidas=[4,8,16,32]
    return memoriasPermitidas[mostrarOpciones(memoriasPermitidas)]
def pedirAlmacenamientoGB():
    print('Ingrese el almacenamiento del dispositivo')
    listaAlmacenamientosDisponibles = [32, 64, 128, 256]
    return listaAlmacenamientosDisponibles[mostrarOpciones(listaAlmacenamientosDisponibles)]
def pedirAlmacenamientoGBAntiguo():
    print('Ingrese el almacenamiento del celular viejo')
    listaAlmacenamientosDisponibles = [2, 4, 6, 8]
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
        mail = input('Ingrese un mail para registrar en el dispositivo:')
        if mail in Email.emailsRegistrados:
            print('No puede tener ese mail. Ya lo tiene otro usuario')
        elif '@' not in mail or '.com' not in mail[-4:]:      #Esta es nuestra humilde validacion de mail
            print('Formato de mail no valido')
        else:
            valido = True
    return mail

def operar(menuOperar):
    '''
    Pide un numero de celular/id para operarlo y lo define como el dispositivo activo
    o se ingresa 1 para volver al menu base
    '''
    existe=False
    while not existe:
        try:
            print('\nDispositivos para operar: ')
            for id in DispositivoElectronico.idUnicos:
                if type(DispositivoElectronico.idUnicos[id])==Celular:
                    print(f'Celular con numero: {DispositivoElectronico.idUnicos[id].numero}')
                elif type(DispositivoElectronico.idUnicos[id])==CelularAntiguo:
                    print(f'Celular antiguo con numero: {DispositivoElectronico.idUnicos[id].numero}')
                elif type(DispositivoElectronico.idUnicos[id])==Tablet:
                    print(f'Tablet con id {id} mail: {DispositivoElectronico.idUnicos[id].get_mail()}')
            opcion=int(input('Ingrese un numero de telefono o el ID de la tablet. Ingrese 1 para volver atras: '))
            if opcion==1 or opcion in DispositivoConRedMovil.numerosUso or (opcion in DispositivoElectronico.idUnicos and type(DispositivoElectronico.idUnicos[opcion])==Tablet):
                existe=opcion
            else:
                print('No hay ningun dispositivo con esa caracteristica') #Consideramos incorrecto ingresar un idUnico valido de un celular cuando a los celulares se deben ingresar por numero telefonico
        except ValueError:
            print('Debe ingresar una opcion valida')
    if existe==1:
        mostrarMenu([('Instanciar',instanciar,[torre]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    else:
        global dispositivoActivo #definimos esta variable global para no estar todo el tiempo pasando el celular activo como parametro
        if existe in DispositivoConRedMovil.numerosUso:
            dispositivoActivo=DispositivoConRedMovil.numerosUso[existe]
        else:
            dispositivoActivo=DispositivoElectronico.idUnicos[existe]
        mostrarMenu(menuOperar)
        
def salir():
    '''
    Este metodo vuelve al menu base desde cualquier otro menu.
    Si el celular no estaba bloqueado lo bloquea.
    '''
    if not dispositivoActivo.bloqueado: 
        dispositivoActivo.bloquear()
    mostrarMenu([('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    
def prender(menuPrender):
    '''
    Prende un celular y si ya estaba prendido no hace nada.
    Muestra el menu prender
    '''
    if dispositivoActivo.apagado:
        dispositivoActivo.prender()
    mostrarMenu(menuPrender)
    
#funciones prender
def apagar():
    '''
    Apaga el celular.
    Muestra el menu operar
    '''
    dispositivoActivo.apagar()
    mostrarMenu([('Prender', prender,[menuPrender]), ('Salir', salir,[])])
    
def desbloquear(menuDesbloquear):
    '''
    Pide el codigo de desbloqueo e intenta desbloquearlo.
    Si falla 6 veces se vuelve al menu base
    Si acierta se muestra el menu desbloquear
    '''
    i=0
    while dispositivoActivo.bloqueado and i<6:
        dispositivoActivo.desbloquear()
        i+=1
    if dispositivoActivo.bloqueado:
        print('Agoto los 6 intentos de desbloqueo')
        mostrarMenu([('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    else:
        mostrarMenu(menuDesbloquear)
        
#funciones desbloquear
def bloquear():
    '''
    Bloquea el celular y muestra el menu prender
    '''
    dispositivoActivo.bloquear()
    prender([('Desbloquear', desbloquear,[menuDesbloquear]), ('Apagar', apagar,[]), ('Salir', salir,[])])
    
def abrirApp():
    '''
    Muestra las aplicaciones que estan descargadas en el celular.
    Valida que la aplicacion este descargada.
    Verifica si tiene internet para las apps que lo necesitan.
    Muestra el menu de la aplicacion.
    Cuando sale del menu de la aplicacion muestra el menu desbloquear
    '''
    dispositivoActivo.verAplicaciones()
    app=input('Ingrese el nombre de la aplicacion: ')
    if app in dispositivoActivo.aplicaciones:
        if app in ('SMS', 'Email', 'App Store') and not dispositivoActivo.internet:
            print(f'No se puede acceder a {app} sin internet')
        else:
            #Antes de mostrar las opciones de cada app, muestro el icono de la misma a traves de matplotlib
            imagenApp = img.imread(dispositivoActivo.aplicaciones[app].icono)
            plt.figure(figsize=(2,2))
            plt.imshow(imagenApp)
            plt.axis('off')
            plt.show(block=False)
            volver = False
            while not volver:
                volver = mostrarMenu(dispositivoActivo.aplicaciones[app].opciones)
            plt.close()
    else:
        print('Esa aplicacion no se encuentra en el celular')
    mostrarMenu([('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])])

def eliminarApp():
    '''
    Intenta eliminar la app. Independientemente de que la elimine o 
    por alguna razon no pueda eliminarla, luego muestra el menu desbloquear
    '''
    try:
        if type(dispositivoActivo)==CelularAntiguo:
            print('Este tipo de celular no permite eliminar aplicaciones')
        else:
            dispositivoActivo.borrarAplicacion()
    except ValueError as e:
        print(e)
    finally:
        mostrarMenu([('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])])

#Main
try:
    with open('idDispositivos.pkl', 'rb') as archivo:
        DispositivoElectronico.idUnicos = pickle.load(archivo)
        
    with open('torre.pkl', 'rb') as archivo:
        torre: Torre = pickle.load(archivo)
        
    #actualiza los objetos del diccionario para que apunten a la misma direccion y llena los atributos de clase que se iban agregando con la instanciacion
    for dispositivo in DispositivoElectronico.idUnicos.values():
        if isinstance(dispositivo,DispositivoConRedMovil):
            DispositivoConRedMovil.numerosUso[dispositivo.numero]=dispositivo
            if dispositivo.numero in torre.telefonosRegistrados:
                torre.telefonosRegistrados[dispositivo.numero]=dispositivo
        if isinstance(dispositivo,DispositivoInteligente):
            Email.emailsRegistrados[dispositivo.aplicaciones['Email'].miMail]=dispositivo.aplicaciones['Email']
                
    # actualiza la torre dentro de cada celular ya que apunta hacia la de la ejecucion previa 
    for celular in DispositivoConRedMovil.numerosUso.values():
        celular.aplicaciones['Telefono'].torre = torre
        celular.aplicaciones['SMS'].torre = torre
        celular.aplicaciones['Configuracion'].torre = torre
    
    #chequear de que un objeto tiene mismo id en todos los diccionarios
    # print(id(DispositivoElectronico.idUnicos[1000]))
    # print(id(DispositivoConRedMovil.numerosUso[1161577917]))
    # print(id(torre.telefonosRegistrados[1161577917]))
    # print()
    # print(id(DispositivoElectronico.idUnicos[1002]))
    # print(id(DispositivoConRedMovil.numerosUso[1167671659]))
    # print(id(torre.telefonosRegistrados[1167671659]))
    
    # chequeo de que la torre es la misma para todos    
    # print(id(Celular.numerosUso[1167671659].aplicaciones['Telefono'].torre))
    # print(id(Celular.numerosUso[1167671659].aplicaciones['SMS'].torre))
    # print(id(Celular.numerosUso[1161577917].aplicaciones['Telefono'].torre))
    # print(id(Celular.numerosUso[1161577917].aplicaciones['SMS'].torre))
    # print(id(torre))
    
    #chequeo de que un chat tiene el mismo id en los 2 telefonos
    # print(id(Celular.numerosUso[1167671659].aplicaciones['SMS'].misChats[1161577917]))
    # print(id(Celular.numerosUso[1161577917].aplicaciones['SMS'].misChats[1167671659]))
    
    #chequeo de que una llamada tiene el mismo id en los 2 telefonos
    # print(id(Celular.numerosUso[1167671659].aplicaciones['Telefono'].enLlamada))
    # print(id(Celular.numerosUso[1161577917].aplicaciones['Telefono'].enLlamada))
    
    #chequeo de que un mail tiene el mismo id en los 2 telefonos
    # print(id(Celular.numerosUso[1167671659].aplicaciones['Email'].bandejaEntrada[0]))
    # print(id(DispositivoElectronico.idUnicos[1001].aplicaciones['Email'].bandejaEnviados[0]))
    
    # instanciacion previa a usar pickle:    
    # torre=Torre()
    # CelularAntiguo('karina','nokia pluma','version 1',4,4,1161577917,torre)
    # Tablet('tomas','iPad5','version 1',8,256,1234,'tomas@gmail.com')
    # archivo = 'MemoriaCelulares.csv'
    # lectorCSV(archivo, torre) #trae a todos los telefonos instanciados previamente
    # for dispositivo in DispositivoElectronico.idUnicos.values(): #activa estos metodos a todos los celulares por practicidad
    #     dispositivo.apagado=False
    #     dispositivo.internet=True
    #     if isinstance(dispositivo,DispositivoConRedMovil):
    #         dispositivo.redMovil=True
    
    menuDesbloquear = [('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])]
    menuPrender=[('Desbloquear', desbloquear,[menuDesbloquear]), ('Apagar', apagar,[]), ('Salir', salir,[])]
    menuOperar=[('Prender', prender,[menuPrender]), ('Salir', salir,[])]
    menuBase=[('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])]
    
    try:
        mostrarMenu(menuBase) #se ejecuta el menu
    except BaseException as e:
        print(f'Error no esperado. Error: {e}')

    #chequeo que la torre tenga todo antes de guardar el objeto torre
    # if isinstance(torre, Torre):
    #     print(torre.telefonosRegistrados)
    #     print(torre.registroDeLlamadas)
    #     print(torre.registroDeMensajes)
    #     print(torre.mensajesPendientes)
    
    #escritura del archivo previo a usar pickle:    
    # sobreescribirCSV(archivo)
    
    with open('idDispositivos.pkl', 'wb') as archivo:
        pickle.dump(DispositivoElectronico.idUnicos, archivo)
        
    with open('torre.pkl', 'wb') as archivo:
        pickle.dump(torre, archivo)
    
except ValueError:
    print('Error grave. Comunicarse.')