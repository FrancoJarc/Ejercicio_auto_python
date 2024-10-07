from auto import Automovil
from vehiculo import Vehiculo

class AutomovilVolador(Vehiculo):
    def __init__(self, color, marca, aceleracion, velocidad,_año,__modelo):
        super().__init__()
        self.color=color
        self.marca=marca
        self.aceleracion=aceleracion
        self.velocidad=velocidad
        self._año=_año
        self.__modelo=__modelo
        self.esta_volando = True
        self.ruedas=0


    def Vuela(self):
        print(f"Vuela: {self.esta_volando}")
    
    def Aterriza(self):
        self.esta_volando= False
        print(f"Aterriza: {self.esta_volando}")

    def __str__(self):
        return f"Automóvil: {self.marca}, Color: {self.color}, Aceleración: {self.aceleracion}, Velocidad: {self.velocidad}, Esta Volando: {self.esta_volando}"

    def datos(self):
        print(f"AutomovilVolador con {self.ruedas}")
