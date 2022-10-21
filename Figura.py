import this
from xml.etree.ElementTree import tostring


class Figura():
    def __init__(self, nombre,color):
        self.__nombre = nombre
        self.__color = color

    # Setters
    def setNombre(self,nom):
        self.__nombre = nom
    
    def setColor(self,col):
        self.__color = col

    # Getters
    def getNombre(self):
        return self.__nombre

    def getColor(self):
        return self.__color
    
    # ToString
    def toString(self):
        print('--------------------------')
        print('Nombre: ',self.getNombre())
        print('Color: ',self.getColor())
