"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

nota = int(input('Digite uma nota, entre 0 a 10: '))

while (nota < 0) or (nota > 10):
    print('Nota inválida.')
    nota = int(input('Digite uma nota, entre 0 a 10: '))
print('Nota válida, obrigada!')