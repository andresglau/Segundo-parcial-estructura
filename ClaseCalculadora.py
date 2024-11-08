from ClaseAplicacion import Aplicacion

class Calculadora(Aplicacion):
    nombre='Calculadora'
    icono=None
    
    def __init__(self):
        super().__init__()
        self.opciones=[('Operar',self.operar,[]),
                       ('Volver a pantalla de inicio', self.volver, [])]
        
    def operar(self):
        while True:
            try:
                num1 = float(input("Ingresa el primer numero: "))
                num2 = float(input("Ingresa el segundo numero: "))
                break
            except ValueError:
                print('No ingreso un numero')
        operador=False
        while not operador:
            operador=input('Ingrese el operador (+ - * /): ')
            if operador not in '+-*/' or len(operador)!=1:
                operador=False
        if operador=='+':
            print(f'{num1} + {num2} = {num1+num2}')
        elif operador=='-':
            print(f'{num1} - {num2} = {num1-num2}')
        elif operador=='*':
            print(f'{num1} * {num2} = {num1*num2}')
        elif operador=='/':
            try:
                if num2==0:
                    raise ValueError('No se puede dividir por 0')
                print(f'{num1} / {num2} = {num1/num2}')
            except ValueError as e:
                print(e)