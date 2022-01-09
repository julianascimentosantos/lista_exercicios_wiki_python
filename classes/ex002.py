"""
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novolado):
        self.lado = novolado

    def mostrarLado(self):
        return print(self.lado)

    def calcularArea(self):
        area = self.lado * 4
        return print(area)

