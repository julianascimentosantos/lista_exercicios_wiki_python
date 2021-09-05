"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

f_graus = int(input('Temperatura em graus Fahtenheit: '))


def transforma_f_em_c(far):
    cel = 5 * ((far-32) / 9)
    return print('Temperatura equivalente em graus Celsius: {}º.'.format(cel))


transforma_f_em_c(f_graus)
