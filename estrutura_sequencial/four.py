"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

from math import *

n1 = (int(input('nota 1: ')))
n2 = (int(input('nota 2: ')))
n3 = (int(input('nota 3: ')))
n4 = (int(input('nota 4: ')))

media = (n1+n2+n3+n4)/4

print('A média das notas é: {}'.format(media))

