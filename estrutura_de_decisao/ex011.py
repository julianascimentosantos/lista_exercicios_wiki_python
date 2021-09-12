"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
1. salários até R$ 280,00 (incluindo) : aumento de 20%
2. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
3. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
4. salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""


def aumento_salario(sal_atual):
    if sal_atual <= 280:
        percentual = 20
        novo_sal = sal_atual * 1.2
    elif 280 < sal_atual <= 700:
        percentual = 15
        novo_sal = sal_atual * 1.15
    elif 700 < sal_atual <= 1500:
        percentual = 10
        novo_sal = sal_atual * 1.1
    else:
        percentual = 5
        novo_sal = sal_atual * 1.05
    print(f'Salário anterior: {sal_atual:.2f}\n'
          f'Percentual de aumento: {percentual}%\n'
          f'Valor do aumento: {(novo_sal - sal_atual):.2f}\n'
          f'Novo Salário: {novo_sal:.2f}\n')


aumento_salario(250)
aumento_salario(280)
aumento_salario(500)
aumento_salario(700)
aumento_salario(1000)
aumento_salario(1500)
aumento_salario(2000)