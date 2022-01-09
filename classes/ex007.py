"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""


class Tamagushi:
    def __init__(self, name, hungry, healthy, age):
        self.name = name
        self.hungry = hungry
        self.healthy = healthy
        self.age = age

    def update_name(self, new_name):
        self.name = new_name
        return self.name

    def update_hungry(self, new_hungry):
        self.hungry = new_hungry
        return self.hungry

    def update_healthy(self, new_healthy):
        self.healthy = new_healthy
        return self.healthy

    def update_age(self, new_age):
        self.age = new_age
        return self.age

    def mood(self):
        if self.hungry >= 70 and self.healthy >= 70:
            return "I'm happy!"

        elif self.hungry >= 50 and self.healthy >= 50:
            return "I'm not so good!"

        elif self.hungry >= 30 and self.healthy >= 30:
            return "I'm very angry!"

        else:
            return "I'm so weak that I can't answer!"
