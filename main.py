from auto import Automovil
from autovolador import AutomovilVolador
from vehiculo import Vehiculo
from suma.suma import sumar
from suma.suma import sumar
from base_Datos.mi_bd import crear_tabla, insertar_auto, leer_vehiculos



"""""
auto1= Automovil("Rojo", "Toyota", 5.5, 120)
print(f"Velocidad: {auto1.velocidad} y aceleracion {auto1.aceleracion}")
auto1.acelera()
print(f"Velocidad: {auto1.velocidad} y aceleracion {auto1.aceleracion}")

print(autoVolador)

sumar(2,2)

print(f"Color: {auto1.getColor()}.\nMarca: {auto1.getMarca()}.\nVelocidad:: {auto1.getVelocidad()}. \nAceleracion {auto1.getAceleracion()}. \nAño: {auto1.getAño()}.\n Modelo: {auto1.getModelo()}")

print(f"Año: {auto1.getAño()}.\n Modelo: {auto1.getModelo()}")
auto1.setAño(2010)
auto1.setModelo("Falcon")
print(f"Año: {auto1.getAño()}.\n Modelo: {auto1.getModelo()}")

auto1=  Automovil("Rojo", "Toyota", 5.5, 120, 2018, "Corolla")
autoVolador= AutomovilVolador("Amarillo", "Toyota", 8.0, 125, 2025, "AeroCar")

def DevolverDatos(vehiculo):
    vehiculo.datos()

DevolverDatos(auto1)
DevolverDatos(autoVolador)


"""

crear_tabla()

 # Insertar un auto de ejemplo
insertar_auto('Amarillo', 'Ford', 2.5, 150, 2020, 'Ecosport')

leer_vehiculos()