"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
1. salário bruto.
2. quanto pagou ao INSS.
3. quanto pagou ao sindicato.
4. o salário líquido.
5. calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""


salario_hora = float(input('Salário hora: '))
horas = float(input('Horas trabalhadas: '))


def salario_mensal(salario_hora, horas):
    salario_bruto = salario_hora * horas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato
    return print(f'+ Salário Bruto : R$ {salario_bruto}\n- IR (11%) : R$ {ir}\n- INSS (8%) : R$ {inss}\n- Sindicato ( '
                 f'5%) : R$ {sindicato}\n= Salário Liquido : R$ {salario_liquido}')


salario_mensal(salario_hora, horas)

