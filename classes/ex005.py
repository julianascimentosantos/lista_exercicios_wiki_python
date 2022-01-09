"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.
"""


class Account:
    def __init__(self, account_number: int, name: str, balance: int = 0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def update_name(self, new_name: str):
        self.name = new_name

    def deposit(self, value: float):
        self.balance = self.balance + value

    def withdraw(self, value: float):
        self.balance = self.balance - value
