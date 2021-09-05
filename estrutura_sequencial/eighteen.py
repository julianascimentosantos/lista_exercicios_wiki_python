"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
import math

arquivo = float(input('Tamanho do arquivo em MB: '))
velocidade = float(input('Velocidade do link de Internet em Mbps: '))


def tempo_download(arq, vel):
    tempo = math.ceil(arq / vel)
    return print('Tempo aproximado de download: {} segundos.'.format(tempo))


tempo_download(arquivo, velocidade)

