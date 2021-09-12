"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novacor):
        self.cor = novacor

    def mostraCor(self, cor):
        return self.cor


# Como chamar a classe

a = Bola('azul', 1.2, 'plastico')
print(a.cor)
print(a.circunferencia)
print(a.material)

a.trocaCor('rosa')
print(a.cor)