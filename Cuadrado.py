from Figura import *

class Cuadrado(Figura):

    def __init__(self, nombre, color, base, altura):
        super().__init__(nombre, color)
        self.__base = base
        self.__altura = altura

        # Setters
    def setBase(self,base):
        self.__base = base

    def setAltura(self,altura):
        self.__altura = altura

        # Getters
    def getBase(self):
        return self.__base

    def getAltura(self):
        return self.__altura

    # toString
    def toString(self):
        super().toString()
        print('Base: ',self.__base)
        print('Altura: ',self.__altura)
        print('--------------------------')


    def calcularArea(b,a):
        area = b * a
        return area
