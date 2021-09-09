"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

from estrutura_de_decisao import ex017

data = str(input('Digite uma data no formato dd/mm/aaaa: '))

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])


def validate_month(dia, mes, ano):
    valido = False

    meses31 = [1, 3, 5, 7, 8, 10, 12]
    meses30 = [4, 6, 9, 11]

    if mes in meses31 and dia <= 31:
        valido = True
    elif mes in meses30 and dia <= 30:
        valido = True
    elif mes == 2:
        if ex017.ano_bisexto(ano) is True and dia <= 29:
            valido = True
        elif dia <= 28:
            valido = True

    if (valido):
        print('Data Válida.')
    else:
        print('Data Inválida.')


validate_month(dia, mes, ano)
