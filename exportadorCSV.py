import csv
from ClaseCelular import Celular
from ClaseTorre import Torre

def lectorCSV(archivo, torre: Torre):
    '''
    Lee las 7 columnas de un CSV con los datos que requiere la instanciacion de un celular
    e instancia un objeto Celular. Requiere que se le pase como parametro un objeto de clase Torre
    '''
    try:
        with open(archivo, 'r') as file:
            lector = csv.reader(file)
            for linea in lector:
                Celular(linea[0], linea[1], linea[2], int(linea[3]),
                        int(linea[4]), int(linea[5]), int(linea[6]),
                        linea[7], torre)
    except FileNotFoundError:
        print('Aun no existe el archivo')

def sobreescribirCSV(archivo):
    '''
    Sobreescribe un CSV con los datos de cada celular que fue usado durante el programa.
    '''
    with open(archivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for celular in Celular.numerosUso.values():
            writer.writerow([celular.nombre, celular.modelo, celular.version, celular.memoriaRAM,
                            celular.almacenamiento, celular.numero, celular.codigo,
                            celular.get_mail()])