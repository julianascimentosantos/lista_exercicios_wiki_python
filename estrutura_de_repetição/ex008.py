"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numeros = []

for i in range(0, 5):
    num = int(input('Informe um número: '))
    numeros.append(num)

soma = sum(numeros)
media = soma / 5

print(soma)
print(media)