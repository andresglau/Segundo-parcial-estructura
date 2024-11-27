import pickle
from ClaseCelular import *
from ClaseTorre import Torre
torre=Torre() #solo para que funcione aca

#codigo a agregar
#para traer
with open('celularNumerosUso.pkl', 'rb') as archivo:
    Celular.numerosUso = pickle.load(archivo)

with open('celularIdUnicos.pkl', 'rb') as archivo:
    Celular.idUnicos = pickle.load(archivo)
    
with open('torreTelefonosRegistrados.pkl', 'rb') as archivo:
    torre.telefonosRegistrados = pickle.load(archivo)
    
with open('torreRegistroDeLlamadas.pkl', 'rb') as archivo:
    torre.registroDeLlamadas = pickle.load(archivo)
    
with open('torreRegistroDeMensajes.pkl', 'rb') as archivo:
    torre.registroDeMensajes = pickle.load(archivo)
    
with open('torreMensajesPendientes.pkl', 'rb') as archivo:
    torre.mensajesPendientes = pickle.load(archivo)

#para guardar
with open('celularNumerosUso.pkl', 'wb') as archivo:
    pickle.dump(Celular.numerosUso, archivo)
    
with open('celularIdUnicos.pkl', 'wb') as archivo:
    pickle.dump(Celular.idUnicos, archivo)
    
with open('torreTelefonosRegistrados.pkl', 'wb') as archivo:
    pickle.dump(torre.telefonosRegistrados, archivo)

with open('torreRegistroDeLlamadas.pkl', 'wb') as archivo:
    pickle.dump(torre.registroDeLlamadas, archivo)
    
with open('torreRegistroDeMensajes.pkl', 'wb') as archivo:
    pickle.dump(torre.registroDeMensajes, archivo)
    
with open('torreMensajesPendientes.pkl', 'wb') as archivo:
    pickle.dump(torre.mensajesPendientes, archivo)
