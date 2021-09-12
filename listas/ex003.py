"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

for i in range(0, 4):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

media = sum(notas) / 4

print(notas)
print(f'Média: {media}')
