from ClaseNodo import *
class Lista():                              #CLASE DE LISTA ENLAZADA COMUN Y CORRIENTE
    def __init__(self,inicio=None):
        self.inicio=inicio

    def esVacia(self):
        return self.inicio==None
    
    def agregarInicio(self,nodo:Nodo):
        if self.esVacia():
            self.inicio=nodo
        else:
            nodo.siguiente=self.inicio
            self.inicio=nodo
            
    def agregarFinal(self,nodo:Nodo):
        if self.esVacia():
            self.inicio=nodo
        else:
            aux=self.inicio
            while aux.siguiente!=None:
                aux=aux.siguiente
            aux.siguiente=nodo
    
    def pop(self):
        if self.esVacia():
            return 'No se puede eliminar el primer dato'
        else:
            dato=self.inicio.dato
            self.inicio=self.inicio.siguiente
            return f'se elimino {dato}'
    
    def pertenece(self, dato):
        esta=False
        aux=self.inicio
        while aux!=None:
            if aux.dato == dato:
                esta=True
                break
            else:
                aux = aux.siguiente
        return esta
    
    def elimino_dato(self, dato):
        aux = self.inicio
        if aux:
            if aux.dato == dato:                #POR SI EL PRIMER ELEMENTO ES EL QUE QUIERO ELIMINAR
                self.inicio = aux.siguiente
                return
            else:
                while aux.siguiente != None:
                    if aux.siguiente.dato == dato:
                        aux.siguiente = aux.siguiente.siguiente
                        return
                    aux = aux.siguiente
        print('No se encontro ese dato')
    
    def longitud(self):
        cont = 0
        aux = self.inicio
        while aux != None:
            cont += 1
            aux = aux.siguiente
        return cont
    
    def __str__(self):
        cadena=''
        aux=self.inicio
        while aux!=None:
            cadena+=str(aux.dato)+' '
            aux=aux.siguiente
        return cadena

a = Lista()
a.agregarInicio(Nodo(1))
a.agregarFinal(Nodo(2))
a.agregarFinal(Nodo(3))
# n1 = a.elimino_dato(3)
