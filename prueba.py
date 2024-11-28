# import pickle
# from ClaseCelular import *
# from ClaseTorre import Torre
# torre=Torre() #solo para que funcione aca

# #codigo a agregar
# #para traer
# with open('celularNumerosUso.pkl', 'rb') as archivo:
#     Celular.numerosUso = pickle.load(archivo)

# with open('celularIdUnicos.pkl', 'rb') as archivo:
#     Celular.idUnicos = pickle.load(archivo)
    
# with open('torreTelefonosRegistrados.pkl', 'rb') as archivo:
#     torre.telefonosRegistrados = pickle.load(archivo)
    
# with open('torreRegistroDeLlamadas.pkl', 'rb') as archivo:
#     torre.registroDeLlamadas = pickle.load(archivo)
    
# with open('torreRegistroDeMensajes.pkl', 'rb') as archivo:
#     torre.registroDeMensajes = pickle.load(archivo)
    
# with open('torreMensajesPendientes.pkl', 'rb') as archivo:
#     torre.mensajesPendientes = pickle.load(archivo)

# #para guardar
# with open('celularNumerosUso.pkl', 'wb') as archivo:
#     pickle.dump(Celular.numerosUso, archivo)
    
# with open('celularIdUnicos.pkl', 'wb') as archivo:
#     pickle.dump(Celular.idUnicos, archivo)
    
# with open('torreTelefonosRegistrados.pkl', 'wb') as archivo:
#     pickle.dump(torre.telefonosRegistrados, archivo)

# with open('torreRegistroDeLlamadas.pkl', 'wb') as archivo:
#     pickle.dump(torre.registroDeLlamadas, archivo)
    
# with open('torreRegistroDeMensajes.pkl', 'wb') as archivo:
#     pickle.dump(torre.registroDeMensajes, archivo)
    
# with open('torreMensajesPendientes.pkl', 'wb') as archivo:
#     pickle.dump(torre.mensajesPendientes, archivo)

# class a:
#     def __init__(self, hola) -> None:
#         self.hola=hola

# class b(a):
#     def __init__(self, hola) -> None:
#         super().__init__(hola)

# class c(a):
#     def __init__(self, hola, mail) -> None:
#         super().__init__(hola)
#         self.mail=mail

# class d(b,c):
#     def __init__(self, hola, mail) -> None:
#         super().__init__(hola)
#         super().__init__(mail)

# h=d(1, 2)

# class Primera:
#     def __init__(self, atributo_a) -> None:
#         self.atributo_a = atributo_a

# class ClaseA(Primera):
#     def __init__(self, atributo_a):
#         super().__init__(atributo_a)
#         print(f"ClaseA inicializada con atributo_a = {self.atributo_a}")

# class ClaseB(Primera):
#     def __init__(self, atributo_a, atributo_b):
#         super().__init__(atributo_a)
#         self.atributo_b = atributo_b
#         print(f"ClaseB inicializada con atributo_b = {self.atributo_b}")

# class ClaseC(ClaseA, ClaseB):  # ClaseC hereda de ClaseA y ClaseB
#     def __init__(self, atributo_a, atributo_b, atributo_c):
#         # Usar super() para manejar el MRO
#         super().__init__(atributo_a)  # Llama al siguiente en MRO
#         # ClaseB.__init__(self, atributo_b)  # Llamada directa para ClaseB (explicación abajo)
#         self.atributo_c = atributo_c
#         print(f"ClaseC inicializada con atributo_c = {self.atributo_c}")

# # Crear una instancia de ClaseC
# objeto = ClaseC(1, 2, 3)


# class a:
#     def __init__(self, hola) -> None:
#         self.hola = hola
#         print(f"Clase a inicializada con hola {self.hola}")

# class b(a):
#     def __init__(self, hola, telefono):
#         super().__init__(hola)
#         self.telefono=telefono
#         print("Clase b inicializada")

# class c(a):
#     def __init__(self, hola, mail) -> None:
#         super().__init__(hola)
#         self.mail = mail
#         print(f"Clase c inicializada con mail {self.mail}")

# class celularNuevo(b, c):
#     def __init__(self, hola, telefono, mail) -> None:
#         super().__init__(hola, telefono)
#         c.__init__(hola, mail)
#         print("Clase d inicializada")

# class CelularViejo(b):
#     def __init__(self, hola, telefono) -> None:
#         super().__init__(hola, telefono)
        
# class ipad(c):
#     def __init__(self, hola, mail) -> None:
#         super().__init__(hola, mail)
# # Crear instancia de la clase d
# h = celularNuevo('hola',1, 2)

# class a:
#     def __init__(self, hola, **kwargs):
#         super().__init__(**kwargs)  # Llamada al siguiente en MRO
#         self.hola = hola
#         print(f"Clase a inicializada con hola {self.hola}")

# class b(a):
#     def __init__(self, hola, telefono, **kwargs):
#         super().__init__(hola=hola, **kwargs)  # Pasar argumentos hacia arriba
#         self.telefono = telefono
#         print(f"Clase b inicializada con telefono {self.telefono}")

# class c(a):
#     def __init__(self, hola, mail, **kwargs):
#         super().__init__(hola=hola, **kwargs)  # Pasar argumentos hacia arriba
#         self.mail = mail
#         print(f"Clase c inicializada con mail {self.mail}")

# class celularNuevo(b, c):
#     def __init__(self, hola, telefono, mail, **kwargs):
#         super().__init__(hola=hola, telefono=telefono, mail=mail, **kwargs)  # MRO resuelve el orden
#         print("Clase celularNuevo inicializada")

# class CelularViejo(b):
#     def __init__(self, hola, telefono, **kwargs):
#         super().__init__(hola=hola, telefono=telefono, **kwargs)
#         print("Clase CelularViejo inicializada")

# class ipad(c):
#     def __init__(self, hola, mail, **kwargs):
#         super().__init__(hola=hola, mail=mail, **kwargs)
#         print("Clase ipad inicializada")

# # Crear instancia de la clase celularNuevo
# h = celularNuevo("Hola", 123456789, "example@mail.com")

#DESDE ACA
'''
'''
# class DispositivoElectronico:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def __str__(self):
#         return f"Nombre: {self.nombre}"


# class DispositivoConRedMovil(DispositivoElectronico):
#     def __init__(self, nombre, numeroTelefonico):
#         DispositivoElectronico.__init__(self, nombre)
#         self.numeroTelefonico = numeroTelefonico

#     def __str__(self):
#         return f"{super().__str__()}, Número Telefónico: {self.numeroTelefonico}"


# class DispositivoConInternet(DispositivoElectronico):
#     def __init__(self, nombre, mail):
#         DispositivoElectronico.__init__(self, nombre)
#         self.mail = mail

#     def __str__(self):
#         return f"{super().__str__()}, Mail: {self.mail}"


# class Telefono(DispositivoConRedMovil, DispositivoConInternet):
#     def __init__(self, nombre, numeroTelefonico, mail):
#         # Inicializar ambas clases padres
#         DispositivoConRedMovil.__init__(self, nombre, numeroTelefonico)
#         DispositivoConInternet.__init__(self, nombre, mail)

#     def __str__(self):
#         return f"Teléfono -> {DispositivoConRedMovil.__str__(self)}, {DispositivoConInternet.__str__(self)}"


# # Ejemplo de uso
# dispositivo = DispositivoElectronico("Tablet")
# print(dispositivo)

# red_movil = DispositivoConRedMovil("Smartphone", "123456789")
# print(red_movil)

# internet = DispositivoConInternet("Laptop", "ejemplo@mail.com")
# print(internet)

# telefono = Telefono("iPhone", "555444333", "usuario@iphone.com")
# print(telefono)

class DispositivoElectronico:
    def __init__(self, common_attr, **kwargs):
        super().__init__(**kwargs)  # Llama al siguiente en el MRO
        self.common_attr = common_attr
        print(f"Base inicializada con common_attr = {self.common_attr}")


class DispositivoConRedMovil(DispositivoElectronico):
    def __init__(self, common_attr, a_attr, **kwargs):
        super().__init__(common_attr=common_attr, **kwargs)  # Llama al siguiente
        self.a_attr = a_attr
        print(f"A inicializada con a_attr = {self.a_attr}")


class DispositivoConInternet(DispositivoElectronico):
    def __init__(self, common_attr, b_attr, **kwargs):
        super().__init__(common_attr=common_attr, **kwargs)  # Llama al siguiente
        self.b_attr = b_attr
        print(f"B inicializada con b_attr = {self.b_attr}")


class CelularNuevo(DispositivoConRedMovil, DispositivoConInternet):
    def __init__(self, common_attr, a_attr, b_attr, **kwargs):
        super().__init__(common_attr=common_attr, a_attr=a_attr, b_attr=b_attr, **kwargs)  # MRO lo gestiona
        print("C inicializada")

c = CelularNuevo('iPhone', '11223344455','i@gmail.com')
print(c.common_attr, c.a_attr, c.b_attr)