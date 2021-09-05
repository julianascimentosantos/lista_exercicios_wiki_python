"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

c_graus = int(input('Temperatura em graus Celsius: '))


def transforma_c_em_f(cel):
    far = (cel * 9/5) + 32
    return print('Temperatura equivalente em graus Fahrenheit: {}º.'.format(far))


transforma_c_em_f(c_graus)

