"""
https://wiki.python.org.br/EstruturaDeDecisao
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math


a = float(input('Valor de a: '))
if a == 0:
    print('O valor do a não pode ser zero.')
else:
    b = float(input('Valor de b: '))
    c = float(input('Valor de c: '))
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('Delta menor que 0. A equação não possui raizes reais.')
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta igual a 0. Raiz = {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Raizes: {raiz1} e {raiz2}.')

