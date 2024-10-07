from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, color, marca,aceleracion,velocidad,_año,__modelo):
        self.color=color
        self.marca=marca
        self.aceleracion=aceleracion
        self.velocidad=velocidad
        self.ruedas=4
        self._año=_año
        self.__modelo=__modelo

    def getColor(self):
        return self.color

    def getMarca(self):
        return self.marca

    def getAceleracion(self):
        return self.aceleracion

    def getVelocidad(self):
        return self.velocidad

    def getAño(self):
        return self._año

    def getModelo(self):
        return self.__modelo  

    def setColor(self, color):
        self.color = color

    def setMarca(self, marca):
        self.marca = marca

    def setAceleracion(self, num):
        self.aceleracion = num

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def setAño(self, año):
        self._año = año  

    def setModelo(self, modelo):
        self.__modelo = modelo  


    def setAceleracion(self,num):
        self.aceleracion=num
        print(f"Aceleracion actual: {self.aceleracion}")

    def getAceleracion(self):
        print(f"Aceleracion actual: {self.aceleracion}")

    def acelera(self):
        self.aceleracion=self.aceleracion+1
        self.velocidad=self.velocidad+1

    def datos(self):
        print(f"Automovil con {self.ruedas}")
    


