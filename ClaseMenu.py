from ClaseCelular import Celular
from ClaseEmail import Email

#metodos comunes de menu
def mostrarMenu(lista):
    nuevaLista=list(map(lambda tupla: tupla[0],lista))
    for i, opcion in enumerate(nuevaLista):
        print(i,opcion)
    opcion=input('Ingrese la opcion: ')
    while not validarOpcion(opcion, lista):
        opcion=input('Ingrese la opcion: ')
    ejecutarOpcion(opcion,lista)

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
    lista[int(opcion)][1](*lista[int(opcion)][2])

#a diferencia de mostrarMenu, este no ejecuta la opcion sino que la devuelve
def mostrarOpciones(lista):
    for i, opcion in enumerate(lista):
        print(i,opcion)
    opcion=input('Ingrese la opcion: ')
    while not validarOpcion(opcion, lista):
        opcion=input('Ingrese la opcion: ')
    return int(opcion)

#funciones especificas
def salir():
    print("Programa terminado")
    
#FuncionInstanciar
def instanciar():
    celu = Celular(pedirNombre(), pedirModelo(),pedirVersion(),pedirMemoriaRAM(),pedirAlmacenamientoGB(),pedirNumero(), pedirCodigo(), pedirMail())
    mostrarMenu([('Instanciar',instanciar,[]),('Operar','',[]),('Salir',salir,[])])

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
        if len(numero)!=10 or numero[:2]!='11' or numero[2]=='0' or not numero.isdigit():
            print('numero de celular incorrecto. Debe tener el siguiente formato: 1123456789')
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

menuBase=[('Instanciar',instanciar,[]),('Operar','',[]),('Salir',salir,[])]




#main
mostrarMenu(menuBase)
