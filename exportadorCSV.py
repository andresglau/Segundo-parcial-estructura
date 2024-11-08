import csv
# from ClaseCelular import *

#nombre, almacenamiento, ((numEmisor, numReceptor, empezoLlamada, terminoLlamada, duracion),...), 
def exportadorCSV():
    file = 'archivoGuardadoCelulares.csv'
    lector = csv.reader(file)
    for linea in lector:
        celu = (linea[1], linea[2])
        MiAppTelefono = celu.aplicaciones['Telefono']
        datosTelefono = tuple(linea[3])

fd = open('PROBANDO.CSV', 'w')
fd.write('nombre,almacenamiento\n')
fd.write('"a,4,op","b,5,8"')
fd.close()

fd = open('PROBANDO.CSV', 'r')
file = csv.reader(fd)
for linea in file:
    for elem in linea:
        telefonos = elem.split(',')
        print(telefonos)
fd.close()