"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
numeros = []

for a in range(num1 + 1, num2):
    numeros.append(a)
soma = sum(numeros)
print(numeros)
print(soma)