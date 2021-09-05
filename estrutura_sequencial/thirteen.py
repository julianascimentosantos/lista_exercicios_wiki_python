"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""


def calcula_peso_ideal(altura, sexo):
    if sexo.upper() == 'M':
        peso_ideal = (72.7*altura) - 58
        return print('Peso ideal homem com altura {}: {}'.format(altura, peso_ideal))
    else:
        peso_ideal = (62.1*altura) - 44.7
        return print('Peso ideal mulher com altura {}: {}'.format(altura, peso_ideal))


calcula_peso_ideal(1.66, 'f')