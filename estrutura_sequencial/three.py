"""
Faça um Programa que peça dois números e imprima a soma.
"""


def somar(num1, num2):
    soma = [num1, num2]
    return print('A soma dos dois números é {}.'.format(sum(soma)))


print('---------- SOME 2 NÚMEROS ----------')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

somar(n1, n2)
