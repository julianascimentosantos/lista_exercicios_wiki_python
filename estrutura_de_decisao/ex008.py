"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

p1 = float(input('Preço do produto 1: '))
p2 = float(input('Preço do produto 2: '))
p3 = float(input('Preço do produto 3: '))

if p1 < p2 and p1 < p3:
    print(f'O produto que você deve comprar é: Produto 1.')
elif p2 < p3 and p2 < p1:
    print(f'O produto que você deve comprar é: Produto 2.')
else:
    print(f'O produto que você deve comprar é: Produto 3.')

