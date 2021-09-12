"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
2. A mensagem "Reprovado", se a média for menor do que sete;
3. A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
from statistics import mean


def media_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(media)
    if media < 7:
        print('Reprovado')
    elif media == 10:
        print('Aprovado com Distinção')
    else:
        print('Aprovado')



media_notas(10, 8)
media_notas(2, 5)
media_notas(5, 5)
media_notas(8, 5)
media_notas(7, 7)
media_notas(10, 10)
media_notas(6.9, 6.9)
