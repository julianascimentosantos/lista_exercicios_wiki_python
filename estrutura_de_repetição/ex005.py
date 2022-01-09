"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

a = int(input('População país A: '))
b = int(input('População país B: '))
taxa_a = float(input('Taxa de crescimento país A: '))
taxa_b = float(input('Taxa de crescimento país B '))
anos = 0

while a < b:
    a = a * (1 + (taxa_a / 100))
    b = b * (1 + (taxa_b / 100))
    anos += 1

print(f'anos {anos}\n'
      f'população país A: {a}\n'
      f'população país B: {b}')
