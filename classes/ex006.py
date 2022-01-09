"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o nível do volume permanecem dentro de faixas válidas.
"""


class Television:
    def __init__(self, channel: int, volume: int = 0):
        self.channel = channel
        self.volume = volume

    def increase_volume(self, increase: int):
        self.volume = self.volume + increase
        if self.volume > 100:
            self.volume = 100

    def decrease_volume(self, decrease: int):
        self.volume = self.volume - decrease
        if self.volume < 0:
            self.volume = 0

    def channel_number(self, new_channel: int):
        self.channel = new_channel
