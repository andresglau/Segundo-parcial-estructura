def validarFormatoNumTelefono(numTelefono: str):
    if len(numTelefono)!=10 or numTelefono[:2]!='11' or numTelefono[2]=='0' or not numTelefono.isdigit():
        print('Numero de celular incorrecto. Debe tener el siguiente formato: 1123456789')
        return True
    return False
