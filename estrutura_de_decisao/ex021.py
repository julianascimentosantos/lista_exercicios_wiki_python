"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

valor = float(input('Valor de saque (valor mínimo: R$10 e valor máximo: R$600: '))

if valor < 10 or valor > 600:
    print('Valor incorreto.')
else:
    nota100 = nota50 = nota10 = nota5 = nota1 = 0
    nota1 = int(valor % 10)
    nota10 = int((valor // 10) % 10)
    nota100 = int((valor // 100) % 10)

    if nota1 >= 5:
        nota5 += 1
        nota1 -= 5

    if nota10 >= 5:
        nota50 += 1
        nota10 -= 5

    print(f'Para sacar a quantia de R${valor:.2f} será utilizado: \n{nota100} notas de R$100 \n{nota50} notas de R$50\n'
          f'{nota10} notas de R$10 \n{nota5} notas de R$5 \n{nota1} notas de R$1')
