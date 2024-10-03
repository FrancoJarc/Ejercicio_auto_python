from auto import Automovil
from autovolador import AutomovilVolador
from suma.suma import sumar


"""""
auto1= Automovil("Rojo", "Toyota", 5.5, 120)
print(f"Velocidad: {auto1.velocidad} y aceleracion {auto1.aceleracion}")
auto1.acelera()
print(f"Velocidad: {auto1.velocidad} y aceleracion {auto1.aceleracion}")

autoVolador= AutomovilVolador("Amarillo","Toyota",8.0,125)
print(autoVolador)

sumar(2,2)

print(f"Color: {auto1.getColor()}.\nMarca: {auto1.getMarca()}.\nVelocidad:: {auto1.getVelocidad()}. \nAceleracion {auto1.getAceleracion()}. \nAño: {auto1.getAño()}.\n Modelo: {auto1.getModelo()}")
"""

auto1= Automovil("Rojo", "Ford", 5.5, 120,2018, "Fiesta")
print(f"Año: {auto1.getAño()}.\n Modelo: {auto1.getModelo()}")
auto1.setAño(2010)
auto1.setModelo("Falcon")
print(f"Año: {auto1.getAño()}.\n Modelo: {auto1.getModelo()}")