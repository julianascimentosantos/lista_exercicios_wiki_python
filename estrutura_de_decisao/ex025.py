"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

pergunta1 = input('Telefonou para a vítima? ').upper()
pergunta2 = input('Esteve no local do crime? ').upper()
pergunta3 = input('Mora perto da vítima? ').upper()
pergunta4 = input('Devia para a vítima? ').upper()
pergunta5 = input('Já trabalhou com a vítima? ').upper()

resp = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
part = 0

for r in resp:
    if r == 'SIM':
        part += 1

if part == 2:
    print('Suspeita')
elif part == 3 or part == 4:
    print('Cúmplice')
elif part == 5:
    print('Assassino')
else:
    print('Inocente')

