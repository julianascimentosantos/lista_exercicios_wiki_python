"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = str(input('Nome: '))
idade = int(input('Idade: '))
salario = float(input('Salário: '))
sexo = str(input('Sexo: '))
estado_civil = str(input('Estado Civil: '))

while len(nome) < 3:
    nome = str(input('O nome não pode ter menos de 3 caracteres, digite novamente. Nome: '))

while (idade < 0) or (idade > 150):
    idade = int(input('Escolha uma idade entre 0 a 150 anos. Idade: '))

while salario < 0:
    salario = float(input('Digite um salário maior que R$0,00. Salário: '))

while sexo not in 'fmFM':
    sexo = str(input('Sexo inválido, digite F ou M. Sexo: '))

while estado_civil not in 'scvdSCVD':
    estado_civil = str(input('Estado Civil inválido, digite S, C, V ou D. Estado Civil: '))
