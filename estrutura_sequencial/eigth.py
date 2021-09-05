"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

salario_hora = float(input('Salário por hora: '))
horas = float(input('Horas trabalhadas no mês: '))


def calcular_salario_mensal(sal, hr):
    salario_mensal = sal * hr
    return print(salario_mensal)

calcular_salario_mensal(salario_hora, horas)



