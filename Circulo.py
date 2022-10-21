from Figura import * 

class Circulo(Figura):

    def __init__(self, nombre, color, radio):
        super().__init__(nombre, color)
        self.__radio = radio

    # Setters
    def setRadio(self,radio):
        self.__radio = radio

    # Getters
    def getRadio(self):
        return self.__radio

    def toString(self):
        super().toString()
        print('Radio: ',self.__radio)
        print('--------------------------')

    def calcularArea(radio):
        area = 3.14 * radio
        resultado = area * area
        return resultado
