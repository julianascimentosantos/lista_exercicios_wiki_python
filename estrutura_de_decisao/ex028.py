"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

carne = str(input('Tipo de carne: '))
kg = float(input('Quantidade da carne: '))
cartao = str(input('Cartão? ')).upper()

if kg <= 5:
    if carne == 'File Duplo':
        valor = kg * 4.9
    elif carne == 'Alcatra':
        valor = kg * 5.9
    elif carne == 'Picanha':
        valor = kg * 6.9
    else:
        print('Carne informada inválida.')
else:
    if carne == 'File Duplo':
        valor = kg * 5.8
    elif carne == 'Alcatra':
        valor = kg * 6.8
    elif carne == 'Picanha':
        valor = kg * 7.8
    else:
        print('Carne informada inválida.')

if cartao == 'SIM':
    pagar = valor - (valor * 0.05)
else:
    pagar = valor

print(f'Tipo da carne: {carne}\n'
      f'Quantidade: {kg}kg\n'
      f'Preço total: {valor}\n'
      f'Pagamento com cartão Tabajara: {cartao}\n'
      f'Desconto: {valor - pagar}\n'
      f'Valor a pagar: {pagar}')