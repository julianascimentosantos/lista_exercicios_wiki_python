"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

kg_morangos = float(input('Quantidade (em kg) de morangos: '))
kg_macas = float(input('Quantidade (em kg) de maçãs: '))

if kg_morangos <= 5:
    valor_morangos = kg_morangos * 2.5
else:
    valor_morangos = kg_morangos * 2.2

if kg_macas <= 5:
    valor_macas = kg_macas * 1.8
else:
    valor_macas = kg_macas * 1.5

kg_total = kg_morangos + kg_macas
valor_total = valor_morangos + valor_macas

if kg_total > 8 or valor_total > 25:
    valor_total = valor_total - (valor_total * 0.1)

print('Valor total: {}'.format(valor_total))
