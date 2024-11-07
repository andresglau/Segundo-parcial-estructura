from ClaseAplicacion import Aplicacion
class Calculadora(Aplicacion):
    nombre='Calculadora'
    icono=None
    def __init__(self):
      self.ultimoValor=None 
        
    def sumar(self):
        if not self.ultimoValor:
            numero1=input('Numero 1: ')
        else:
            numero1=self.ultimoValor
            
        numero2=input('Numero 2: ')
        return numero1+numero2

        
    def multiplicar(self):
        if not self.ultimoValor:
            numero1=input('Numero 1: ')
        else:
            numero1=self.ultimoValor
            
        numero2=input('Numero 2: ')
        return numero1*numero2

    def resta(self):
        if not self.ultimoValor:
            numero1=input('Numero 1: ')
        else:
            numero1=self.ultimoValor
            
        numero2=input('Numero 2: ')
        return numero1-numero2
    
    def division(self):
        if not self.ultimoValor:
            numero1=input('Numero 1: ')
        else:
            numero1=self.ultimoValor
            
        numero2=input('Numero 2: ')
        return numero1/numero2
    
    
    