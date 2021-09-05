"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
1. comprar apenas latas de 18 litros;
2. comprar apenas galões de 3,6 litros;
3. misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""


import math


metros = float(input('Área em m² a ser pintada: '))
litros = (metros * 1.1) / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)

print(f'A quantidade de latas de tintas a serem compradas é {latas} e o preço total é R${latas * 80}.')
print(f'\nA quantidade de galões de tintas a serem compradas é {galoes} e o preço total é R${galoes * 25}.')

lat = litros // 18
gal = math.ceil((litros - (lat * 18)) / 3.6)

print('\nJuntando latas e galões:')
print(f'A quantidade de latas de tintas a serem compradas é {lat} e o preço total é R${lat * 80}.')
print(f'A quantidade de galões de tintas a serem compradas é {gal} e o preço total é R${gal * 25}.')

