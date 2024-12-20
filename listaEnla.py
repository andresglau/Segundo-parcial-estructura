from nodoListaEnla import Nodo

class Lista():
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
    
    def popLeft(self):
        if self.esVacia():
            return 'No se puede eliminar el primer dato'
        else:
            dato=self.inicio.dato
            self.inicio=self.inicio.siguiente
            return f'se elimino {dato}'
        
    def __str__(self):
        cadena=''
        aux=self.inicio
        cont = 0
        while aux!=None:
            cadena+=str(cont)+': '+str(aux.dato)+'\n'
            aux=aux.siguiente
            cont +=1
        return cadena
        
class ListaMensajes(Lista):
    def __init__(self, inicio=None):
        super().__init__(inicio)
        
    def agregarInicio(self): #redefinir el metodo porque los mensajes solo se agregan al final
        pass
    
    def popLeft(self): #redefinir el metodo porque los mensajes solo se pueden eliminar por indice
        pass
    
    def eliminarMensaje(self, pos: int, miNumero: int):
        aux = self.inicio
        if aux:
            if pos == 0:
                if miNumero == aux.dato.numEmisor:
                    self.inicio = aux.siguiente
                    print(f'Se elimino el mensaje {aux.dato}')
                else:
                    print('No podes eliminar un mensaje que envio la otra persona')
                return
            else:
                i = 1
                while aux.siguiente != None:
                    if i == pos:
                        if miNumero == aux.siguiente.dato.numEmisor:
                            print(f'Se elimino el mensaje {aux.siguiente.dato}')
                            aux.siguiente = aux.siguiente.siguiente
                        else:
                            print('No podes eliminar un mensaje que envio la otra persona')
                        return
                    aux = aux.siguiente
                    i+=1
                print('Posicion fuera de rango')
        else:
            print('No hay mensajes')