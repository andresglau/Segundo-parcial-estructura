import Validaciones
from ClaseTorre import Torre
from ClaseEmail import Email
from ClaseCelular import Celular
from ClaseContacto import Contacto

#metodos comunes de menu
def mostrarMenu(lista):
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
    return lista[int(opcion)][1](*lista[int(opcion)][2])

#a diferencia de mostrarMenu, este no ejecuta la opcion sino que la devuelve
def mostrarOpciones(lista):
    for i, opcion in enumerate(lista):
        print(i,opcion)
    opcion=input('Ingrese la opcion: ')
    while not validarOpcion(opcion, lista):
        opcion=input('Ingrese la opcion: ')
    return int(opcion)

#funciones especificas
def terminar():
    print("Programa terminado")
    
#FuncionInstanciar
def instanciar(torre: Torre, menuOperar):
    celu = Celular(pedirNombre(), pedirModelo(),pedirVersion(),pedirMemoriaRAM(),pedirAlmacenamientoGB(),pedirNumero(), pedirCodigo(), pedirMail(),torre)
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
        elif '@' not in mail or '.com' not in mail[-4:]:      #VALIDAR FORMATO MAIL
            print('Formato de mail no valido')
        else:
            valido = True
    return mail

#funcion operar
def operar(menuOperar):
    existe=False
    while not existe:
        try:
            opcion=int(input('Ingrese un numero de telefono. Ingrese 1 para volver atras: '))
            if opcion==1 or opcion in Celular.numerosUso:
                existe=opcion
        except ValueError:
            print('Debe ingresar una opcion valida')
            #si sobra tiempo printear los telefonos disponibles
    if existe==1:
        mostrarMenu([('Instanciar',instanciar,[torre]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    else:
        global celularActivo #definimos esta variable global para no estar todo el tiempo pasando el celular activo como parametro
        celularActivo=Celular.numerosUso[existe]
        mostrarMenu(menuOperar)
        
def salir():
    if not celularActivo.bloqueado: #siempre que se sale del celular, ese celular se bloquea.
        celularActivo.bloquear()
    mostrarMenu([('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    
def prender(menuPrender):
    if celularActivo.apagado: #un telefono cuando se dejo de operar no se apaga ya que sino no se podria realizar llamadas
        celularActivo.prender()
    mostrarMenu(menuPrender)
    
#funciones prender
def apagar():
    celularActivo.apagar()
    mostrarMenu([('Prender', prender,[menuPrender]), ('Salir', salir,[])])
    
def desbloquear(menuDesbloquear):
    i=0
    while celularActivo.bloqueado and i<6:
        celularActivo.desbloquear()
        i+=1
    if i==6:
        print('Agoto los 6 intentos de desbloqueo')
        mostrarMenu([('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])])
    else:
        mostrarMenu(menuDesbloquear)
        
#funciones desbloquear
def bloquear():
    celularActivo.bloquear()
    prender([('Desbloquear', desbloquear,[menuDesbloquear]), ('Apagar', apagar,[]), ('Salir', salir,[])])
    
def abrirApp():
    celularActivo.verAplicaciones()
    app=input('Ingrese el nombre de la aplicacion: ')
    if app in celularActivo.aplicaciones:
        volver = False
        while not volver:
            volver = mostrarMenu(celularActivo.aplicaciones[app].opciones)
    else:
        print('Esa aplicacion no se encuentra en el celular')
    mostrarMenu([('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])])

def eliminarApp():
    try:
        celularActivo.borrarAplicacion()
    except ValueError as e:
        print(e)
    finally:
        mostrarMenu([('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])])
    
#instancias
torre=Torre()
menuDesbloquear = [('Apagar', apagar, []), ('Bloquear', bloquear, []), ('Abrir App', abrirApp, []), ('Eliminar App', eliminarApp, []), ('Salir', salir, [])]
menuPrender=[('Desbloquear', desbloquear,[menuDesbloquear]), ('Apagar', apagar,[]), ('Salir', salir,[])]
menuOperar=[('Prender', prender,[menuPrender]), ('Salir', salir,[])]
menuBase=[('Instanciar',instanciar,[torre, menuOperar]),('Operar',operar,[menuOperar]),('Terminar',terminar,[])]


#main
andi=Celular('Andi','iphone 15', '1', 8, 64, 1167671659, 1234,'andi@gmail.com',torre)
ichi=Celular('Ichi', 'iphone 15', '1', 8, 64, 1156789023, 1234, 'ichi@gmail.com', torre)
fede=Celular('Fede', 'iphone 15', '1', 8, 64, 1198765432, 1234, 'fede@gmail.com', torre)
manu=Celular('Manu', 'iphone 15', '1', 8, 64, 1123455432, 1234, 'manu@gmail.com', torre)

andi.aplicaciones['Contactos'].contactos={ichi.nombre:Contacto(ichi.nombre,ichi.numero),fede.nombre:Contacto(fede.nombre,fede.numero),manu.nombre:Contacto(manu.nombre,manu.numero)}
andi.aplicaciones['Telefono'].contactos = andi.aplicaciones['Contactos'].contactos
andi.aplicaciones['SMS'].contactos = andi.aplicaciones['Contactos'].contactos
ichi.aplicaciones['Contactos'].contactos={'andi':Contacto('andi',1167671659), 'fede':Contacto('fede',1198765432),'manu':Contacto('manu',1123455432)}
ichi.aplicaciones['Telefono'].contactos = ichi.aplicaciones['Contactos'].contactos
ichi.aplicaciones['SMS'].contactos = ichi.aplicaciones['Contactos'].contactos


for celular in Celular.numerosUso.values():
    torre.agregarTelefono(celular)
    celular.apagado=False
    celular.redMovil=True
    celular.internet=True

try:
    mostrarMenu(menuBase)
except BaseException as e:
    print(f'Error no esperado. Error: {e}')