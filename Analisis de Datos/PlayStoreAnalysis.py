import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

try:
    with open('Analisis de Datos\Play Store Data.csv', 'r', encoding = 'utf-8') as file:
        file.readline()
        lector = csv.reader(file)
        diccionarioCategorias = {}
        diccionarioEdadesCategoria = {}
        for linea in lector:
            '''
            En diccionarioCategorias la clave va a ser una categoria y el valor va a ser un array con todos
            los registros de las apps de esa categoria que haya en el CSV.
            El array que se va a guardar en ese diccionario contendra los datos Rating, Resenas, Tamano, Descargas, Precio
            '''
            if linea[4] == 'Varies with device':        #Registros de tamano que varian con dispositivo se omiten
                pass
            elif linea[5][-1] != '+':                   #Si las instalaciones no terminan en "+" las omitimos porque no respetan el formato estandar
                pass
            else:
                rating = None
                if linea[2]=='NaN':                     #Las aplicaciones que no tienen ratings se les asigna el rating medio de esa categoria hasta ese momento
                    if linea[1] not in diccionarioCategorias:
                        rating = float(0)
                    else:
                        rating = float(np.mean(diccionarioCategorias[linea[1]][:,0], axis = 0))
                line = [float(linea[2]) if linea[2]!='NaN' else rating,                             #Rating
                        float(linea[3]),                                                            #Resenas
                        float(linea[4][:-1])/1000 if linea[4][-1]=='k' else float(linea[4][:-1]),   #Tamano
                        float(linea[5][:-1].replace(',', '') if ',' in linea[5] else linea[5][:-1]), #Descargas                    
                        float(linea[7][1:]) if linea[7]!='0' else float('0'),                       #Precio
                            ]
                if linea[1] not in diccionarioCategorias:
                    diccionarioCategorias[linea[1]]=np.array([line])
                else:
                    diccionarioCategorias[linea[1]]=np.append(diccionarioCategorias[linea[1]], [line], axis = 0)
            
            '''
            Las apps son de una de estas categorias: 'Everyone', 'Teen', 'Everyone 10+', 'Mature 17+', 'Adults only 18+' o 'Unrated'
            Se hace una distincion de que las categorias a las que no pueden acceder niños son 'Mature 17+' y 'Adults only 18+', se pasa un "1" en ese caso
            'Everyone' y 'Everyone 10+' son las que pueden acceder niños, se pasa un "0" en ese caso
            'Unrated' y 'Teen' no son tenidas en cuenta al no ser precisas en su descripcion
            IMPORTANTE: este lo hicimos aparte porque el 'Unrated' y 'Teen' pueden segregar muchos datos y eso no es la idea para el resto de los analisis
            '''
            edad = None
            if linea[8] in ('Adults only 18+', 'Mature 17+'):
                edad = 1
            elif linea[8] in ('Everyone', 'Everyone 10+'):
                edad = 0
            if edad != None:
                if linea[1] not in diccionarioEdadesCategoria:
                    diccionarioEdadesCategoria[linea[1]] = np.array([edad])
                else:
                    diccionarioEdadesCategoria[linea[1]] = np.append(diccionarioEdadesCategoria[linea[1]], [edad])
except FileNotFoundError:
    print('No esta encontrando el archivo')
except:
    print('Ha habido un error mas grave que el referido a la direccion del archivo')
else:
    np.set_printoptions(suppress=True)

    promedioDescargas=[]
    promedioRatings=[]
    cantidadApps = []
    porcentajeGratuitos = []
    tamanoPromedio = []
    for clave in diccionarioCategorias:
        promedioDescargas.append(np.mean(diccionarioCategorias[clave][:,3], axis = 0))      #Promedio de descargas
        promedioRatings.append(np.mean(diccionarioCategorias[clave][:,0], axis = 0))        #Promedio de ratings
        cant = diccionarioCategorias[clave].shape[0]
        cantidadApps.append(cant)                                                           #Cantidad de apps
        porcentajeGratuitos.append(((diccionarioCategorias[clave][:,4]==0).sum()/cant)*100) #Porcentaje de apps gratuitas
        tamanoPromedio.append(np.mean(diccionarioCategorias[clave][:,2], axis= 0))
    
    mensaje = '''
    Grafico 1: Rating promedio vs descargas promedio por app de cada categoria
    Grafico 2: Porcentaje de apps gratuitas por categoria
    Grafico 3: Porcentaje de apps segun edad del contenido
    '''
    print(mensaje)
    opcion = input('¿Que grafico quiere ver? (1,2,3): ')

    #GRAFICO 1 - SCATTER GRAPH
    if opcion=='1':
        grafico_dispersion = plt.scatter(promedioDescargas, promedioRatings, c=cantidadApps, cmap = 'spring')
        plt.colorbar(grafico_dispersion, label = 'Cantidad de apps')
        plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
        plt.gca().xaxis.get_major_formatter().set_scientific(False)
        plt.title('Rating promedio vs descargas promedio por app de cada categoria', pad = 13, fontweight = 'light')
        plt.xlabel('Descargas promedio por app de la categoria', labelpad = 10, fontweight = 'bold')
        plt.ylabel('Rating promedio por app de la categoria', labelpad = 10, fontweight = 'bold')
        plt.xlim(min(promedioDescargas)-1000000, max(promedioDescargas)+2000000)
        plt.ylim(min(promedioRatings)-0.02,max(promedioRatings)+0.02)
        espacios0alMillon = np.arange(0,10000000,2000000)
        espaciosMillonalFinal = np.arange(10000000,30000000,5000000)
        misEspaciados = np.concatenate([espacios0alMillon, espaciosMillonalFinal])
        plt.xticks(misEspaciados, size = 10, rotation = 40)
        percentil_90_descargas=np.percentile(np.array(promedioDescargas),90)
        percentil_10_descargas=np.percentile(np.array(promedioDescargas),10)
        percentil_90_ratings=np.percentile(np.array(promedioRatings),90)
        percentil_10_ratings=np.percentile(np.array(promedioRatings),10)
        for i, categoria in enumerate(diccionarioCategorias):
            if promedioRatings[i] >= percentil_90_ratings or promedioRatings[i] <= percentil_10_ratings or promedioDescargas[i] >= percentil_90_descargas or promedioDescargas[i] <= percentil_10_descargas:
                plt.text(promedioDescargas[i], promedioRatings[i], categoria, size = 7, fontweight = 'bold')
        plt.gca().set_facecolor('lightblue')
        plt.gcf().set_facecolor('yellowgreen')
        plt.tight_layout()
        plt.show()

    #GRAFICO 2 - BAR CHART
    elif opcion=='2':
        categorias = list(diccionarioCategorias.keys())
        porcentajes = np.array(porcentajeGratuitos)
        ordenamiento = sorted(zip(porcentajes, categorias), reverse = True)
        porcentajes, categorias = list(zip(*ordenamiento))
        resto = np.array(list(map(lambda porcentaje: 100-porcentaje, porcentajes)))

        plt.bar(categorias, porcentajes, label = '% apps gratuitas')
        plt.bar(categorias, resto, bottom = porcentajes, label = '% apps pagas')
        plt.ylabel('Porcentaje de apps gratuitas')
        plt.xlabel('Categorias', labelpad=10)
        plt.title('Porcentaje de apps gratuitas por categoria', size = 10, pad = 10, fontweight = 'bold')
        plt.ylim(min(porcentajeGratuitos)-2.0, 100)
        plt.xticks(rotation = 45, ha = 'right', fontsize = 6.5)
        plt.gcf().set_facecolor('linen')
        plt.legend()
        plt.tight_layout()
        plt.show()

    #GRAFICO 3 - PIE CHART
    # porcentajeAppsMayores = np.array(list(map(lambda array: (array.sum()/array.shape[0])*100, diccionarioEdadesCategoria.values())))
    elif opcion=='3':
        for clave in diccionarioEdadesCategoria:
            diccionarioEdadesCategoria[clave] = (diccionarioEdadesCategoria[clave].sum()/diccionarioEdadesCategoria[clave].shape[0])*100

        porcentajeAppsMayores = np.array(list(diccionarioEdadesCategoria.values()))
        condicion = porcentajeAppsMayores > np.median(porcentajeAppsMayores)      #Se toman las categorias con porcentajes mayores a la mediana
        porcentajeAppsMayores = np.extract(condicion, porcentajeAppsMayores)

        etiquetas = ['Apps mayores', 'Apps niños']

        plt.subplots(4,4, figsize=(9,7))
        plt.suptitle('Porcentaje de apps segun edad del contenido', fontweight = 'light', fontsize = 20, ha = 'center')
        for i in range(16):
            plt.subplot(4,4,i+1)
            plt.pie([porcentajeAppsMayores[i], 100-porcentajeAppsMayores[i]], autopct='%1.1f%%', startangle=90)
            plt.title(list(diccionarioEdadesCategoria.keys())[list(diccionarioEdadesCategoria.values()).index(porcentajeAppsMayores[i])], size=10)
        plt.legend(bbox_to_anchor = (1,0.8), labels = etiquetas)
        plt.gcf().set_facecolor('lavenderblush')
        plt.tight_layout()
        plt.show()

    else:
        print('No eligio ninguna opcion valida')
