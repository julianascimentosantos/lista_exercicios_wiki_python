"""
Faça um programa que leia 5 números e informe o maior número.
"""

num = int(input('Digite um número: '))
maior = num

for n in range(0, 4):
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
print(maior)

