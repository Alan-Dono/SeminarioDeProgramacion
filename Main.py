from typing import List
import os
from Cuadrado import Cuadrado
from Figura import Figura
from Controladora import Controladora
''' Todas las clases estan sin sus respectivas validaciones... preferi concentrame en hacer que funcione pero me quedo del todo bien'''
controller = Controladora()
op = -1
figura = []
while op != 0:
    os.system('cls')
    print('1) Crear Cuadrado: ')
    print('2) Crear triangulo: ')
    print('3) Crear Circulo: ')
    print('4) Mostrar Figuras')
    print('5) Calcular area')
    print('0) Fin')
    op = int(input())
    if op == 1:
        figura = controller.crearCuadrado()
    elif op == 2:
        figura = controller.crearTriangulo()
    elif op == 3:
        figura = controller.crearCirculo()
    elif op == 4:
        controller.mostrarLista()
    elif op == 5:
        controller.calcularArea()




