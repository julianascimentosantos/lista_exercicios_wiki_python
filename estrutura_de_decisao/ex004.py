"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = str(input('Digite uma letra: ')).upper()

if letra in 'AEIOU':
    print('É uma vogal.')
elif letra in 'BCDFGHJKLMNPQRSTVWXYZ':
    print('É uma consoante.')
elif len(letra) != 1:
    print('Você não digitou apenas uma letra.')
else:
    print('Não é uma letra.')

