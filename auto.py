class Automovil:
    def __init__(self, color, marca,aceleracion,velocidad):
        self.color=color
        self.marca=marca
        self.aceleracion=aceleracion
        self.velocidad=velocidad
        self.ruedas=4

    def setAceleracion(self,num):
        self.aceleracion=num
        print(f"Aceleracion actual: {self.aceleracion}")

    def getAceleracion(self):
        print(f"Aceleracion actual: {self.aceleracion}")

    def acelera(self):
        self.aceleracion=self.aceleracion+1
        self.velocidad=self.velocidad+1
