"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

valor = int(input('Digite um número para saber o dia da semana (1 a 7): '))


def dia_semana(num):
    if num == 1:
        print('Domingo')
    elif num == 2:
        print('Segunda')
    elif num == 3:
        print('Terça')
    elif num == 4:
        print('Quarta')
    elif num == 5:
        print('Quinta')
    elif num == 6:
        print('Sexta')
    elif num == 7:
        print('Sábado')
    elif num == 8:
        print('Domingo')
    else:
        print('Valor inválido')


dia_semana(valor)