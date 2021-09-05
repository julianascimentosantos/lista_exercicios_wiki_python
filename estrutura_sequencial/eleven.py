"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. o produto do dobro do primeiro com metade do segundo.
2. a soma do triplo do primeiro com o terceiro.
3. o terceiro elevado ao cubo.
"""

first_int = int(input('Digite um número inteiro: '))
second_int = int(input('Digite outro número inteiro: '))
one_float = float(input('Digite um número real: '))

case_one = (first_int * 2) * (second_int / 2)
case_two = (first_int * 3) + one_float
case_three = one_float**3

print('1. o produto do dobro do primeiro com metade do segundo: {}\n' 
      '2. a soma do triplo do primeiro com o terceiro: {} \n'
      '3. o terceiro elevado ao cubo: {}'.format(case_one, case_two, case_three))
