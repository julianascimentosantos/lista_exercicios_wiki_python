"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))


def status_aluno(n1, n2):
    media = (nota1 + nota2) / 2

    if 9 < media <= 10:
        conceito = 'A'
    elif 7.5 < media <= 9:
        conceito = 'B'
    elif 6 < media <= 7.5:
        conceito = 'C'
    elif 4 < media <= 6:
        conceito = 'D'
    elif media <= 4:
        conceito = 'E'
    else:
        conceito = 'Média Inválida'

    if conceito in 'ABC':
        mensagem = 'Aprovado'
    elif conceito in 'DE':
        mensagem = 'Reprovado'

    print(f'NOTA 1: {nota1}\n'
          f'NOTA 2: {nota2}\n'
          f'MÉDIA: {media}\n'
          f'CONCEITO: {conceito}\n'
          f'MENSAGEM: {mensagem}')


status_aluno(nota1, nota2)
