"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = str(input('Nome de usuário: '))
senha = str(input('Nova senha: '))

while senha == usuario:
    print('A Senha não pode ser igual ao Nome de Usuário.')
    usuario = str(input('Nome de usuário: '))
    senha = str(input('Nova senha: '))
print('Cadastro concluido.')