"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

for a in range(num1 + 1, num2):
    print(a, end=' ')