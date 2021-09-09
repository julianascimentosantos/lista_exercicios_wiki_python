"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
* Salário Bruto até 900 (inclusive) - isento
* Salário Bruto até 1500 (inclusive) - desconto de 5%
* Salário Bruto até 2500 (inclusive) - desconto de 10%
* Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

salario_hora = float(input('Salário hora: '))
horas = float(input('Horas trabalhadas no mês: '))
salario_bruto= salario_hora * horas
inss = salario_bruto * 0.10
fgts= salario_bruto * 0.11
sindicato = salario_bruto * 0.03

if 900 < salario_bruto <= 1500:
    percentual = 5
    desconto_ir = salario_bruto * 0.05
elif 1500 < salario_bruto <= 2500:
    percentual = 10
    desconto_ir = salario_bruto * 0.10
elif salario_bruto > 2500:
    percentual = 20
    desconto_ir = salario_bruto * 0.20
else:
    desconto_ir = 0

descontos = inss + sindicato + desconto_ir

print(f'Salário Bruto                   : R$ {salario_bruto:.2f} ({horas} * {salario_hora})\n'
      f'(-) IR ({percentual}%)                    : R$  {desconto_ir:.2f}\n'
      f'(-) INSS (10%)                  : R$  {inss:.2f}\n'
      f'(-) Sindicato (3%)              : R$  {sindicato:.2f}\n'
      f'FGTS (11%)                      : R$  {fgts:.2f}\n'
      f'Total de descontos              : R$  {descontos:.2f}\n'
      f'Salário Liquido                 : R$  {salario_bruto - descontos:.2f}')

