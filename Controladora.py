
import os
from typing import List
from Cuadrado import Cuadrado
from Figura import Figura
from Triangulo import Triangulo
from Circulo import Circulo


class Controladora:

    def __init__(self):
        self.__listaObj = []


    def crearCuadrado(self):
        nom = input('Nombre: ')
        col = input('Color: ')
        bas = int(input('Base: '))
        alt = int(input('Altura: '))
        nuevoCuadrado = Cuadrado(nom,col,bas,alt)
        self.__listaObj.append(nuevoCuadrado)
        return self.__listaObj

    def crearTriangulo(self):
        nom = input('Nombre: ')
        col = input('Color: ')
        bas = int(input('Base: '))
        alt = int(input('Altura: '))
        nuevoTriangulo = Triangulo(nom,col,bas,alt)
        self.__listaObj.append(nuevoTriangulo)
        return self.__listaObj

    
    def crearCirculo(self):
        nom = input('Nombre: ')
        col = input('Color: ')
        rad = int(input('Radio: '))
        nuevoCirculo = Circulo(nom,col,rad)
        self.__listaObj.append(nuevoCirculo)
        return self.__listaObj

    def mostrarLista(self):
        os.system('cls')
        for i in self.__listaObj:
            print(i.toString())
            
    
    def calcularArea(self):
        op = -10
        os.system('cls')
        print('1) De un cuadrado')
        print('2) De un triangulo')
        print('3) De un circulo')
        print('0) Salir')
        while op != 0:
            op = int(input())
            if op == 1:
                b = int(input('Base: '))
                a = int(input('Altura: '))
                area = Cuadrado.calcularArea(b,a)
                print('El area del cuadrado es: ',area)
                input()
            elif op == 2:
                b = int(input('Base: '))
                a = int(input('Altura: '))
                area = Triangulo.calcularArea(b,a)
                print('El area del triangulos es: ',area)
                input()
            elif op == 3:
                r = int(input('Radio: '))
                area = Circulo.calcularArea(r)
                print('El radio del circulo es: ',area)
                input()


