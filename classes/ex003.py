"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_lados(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def mostrar_lados(self):
        return self.comprimento, self.largura

    def calcular_area(self):
        area = self.comprimento * self.largura
        return area

    def calcular_perimetro(self):
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro


c = float(input('Digite o comprimento: '))
l = float(input('Digite a largura: '))

a = Retangulo(c, l)

pisos = a.calcular_area()
rodapes = a.calcular_perimetro()

print(f'Será necessário: {pisos}m² de pisos e {rodapes}m de rodapés.')