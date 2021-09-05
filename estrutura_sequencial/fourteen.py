"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""


def calcula_multa(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4.00
        return print('O excesso de peso foi {} e a multa a pagar é R${}.'.format(excesso, multa))
    else:
        return print('O peso está dentro do regulamento.')


calcula_multa(50)
calcula_multa(150)

