from auto import Automovil

class AutomovilVolador(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad,_año,___modelo):
        super().__init__(color, marca, aceleracion, velocidad,_año,___modelo)
        self.esta_volando = True


    def Vuela(self):
        print(f"Vuela: {self.esta_volando}")
    
    def Aterriza(self):
        self.esta_volando= False
        print(f"Aterriza: {self.esta_volando}")

    def __str__(self):
        return f"Automóvil: {self.marca}, Color: {self.color}, Aceleración: {self.aceleracion}, Velocidad: {self.velocidad}, Esta Volando: {self.esta_volando}"

