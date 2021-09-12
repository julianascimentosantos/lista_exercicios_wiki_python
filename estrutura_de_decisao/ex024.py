"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""


def main():

    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))

    print('Qual operação gostaria de fazer?')
    opcao = int(input('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n'))

    if opcao == 1:
        result = valor1 + valor2
    elif opcao == 2:
        result = valor1 - valor2
    elif opcao == 3:
        result = valor1 * valor2
    elif opcao == 4:
        result = valor1 / valor2
    else:
        print('Opção Inválida.')
        exit()

    print(f'Result = {result}')

    if result % 2 == 0:
        print('Número par.')
    else:
        print('Número ímpar.')

    if result >= 0:
        print('Número positivo.')
    else:
        print('Número negativo.')

    if result == round(result):
        print('Número inteiro.')
    else:
        print('Número decimal')


if __name__ == '__main__':
    main()