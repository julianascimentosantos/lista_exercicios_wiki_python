"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math


metros = float(input('Área em m² a ser pintada: '))
litros = metros / 3
latas = math.ceil(litros / 18)

print(f'A quantidade de latas de tintas a serem compradas é {latas} e o preço total é R${latas * 80}.')
