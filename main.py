from auto import Automovil
from autovolador import AutomovilVolador


auto1= Automovil("Rojo", "Toyota", 5.5, 120)
print(f"Velocidad: {auto1.velocidad} y aceleracion {auto1.aceleracion}")
auto1.acelera()
print(f"Velocidad: {auto1.velocidad} y aceleracion {auto1.aceleracion}")

"""""
autoVolador= AutomovilVolador("Amarillo","Toyota",8.0,125)
print(autoVolador)"""