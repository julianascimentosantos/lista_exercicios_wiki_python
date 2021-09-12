"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Person:
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_old(self):
        if self.age < 21:
            self.height += 0.5

        self.age += 1

    def get_fat(self, kg):
        self.weight += kg

    def lose_weight(self, kg):
        self.weight -= kg

    def grow_up(self, cm):
        self.height += cm

