"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""

num = float(input('Digite um número: '))

if num == round(num):
    print('O número é inteiro.')
else:
    print('O número é decimal.')