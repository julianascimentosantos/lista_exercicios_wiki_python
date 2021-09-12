"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input('Triângulo - Lado 1: '))
lado2 = float(input('Triângulo - Lado 2: '))
lado3 = float(input('Triângulo - Lado 3: '))


def classif_triangulo(l1, l2, l3):

    if l1 == 0 or l2 == 0 or l3 == 0:
        print('Lados inválidos.')
    elif l1 == l2 == l3:
        print('Triângulo Equilátero.')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l3 == l2 != l1:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')


classif_triangulo(lado1, lado2, lado3)

