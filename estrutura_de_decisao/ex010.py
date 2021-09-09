"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""


turno = str(input('Qual o turno que você estuda? \nM para Matutino \nV para Vespertino \nN para Noturno\nDigite: ')).upper()


def imprime_mensagem(turno):
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Valor Inválido!')


imprime_mensagem(turno)
