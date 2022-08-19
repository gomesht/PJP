"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios. """
from tkinter import N


class ContaCorrente:
    def __init__(self,nuemro, nome,saldo = 0) :
        self.numero = nuemro
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self,n_nome):
        n_nome = input("Qual o nome atualizado? ")
        self.nome = n_nome
    def deposito(self):
        valord = input("Quanto deseja depositar: ")
        self.saldo += int(valord)
    def saque(self):
        valors = input("Quanto deseja sacar: ") 
        if self.saldo >= int(valors):
            self.saldo -= int(valors)
        else:
            print("Saldo insuficiente")
conta_1 = ContaCorrente("00001","José")

while True:
    op = input(f"Ola {conta_1.nome}, o que deseja?\n1 - Informações da conta\n2 - Depósito\n3 - Saque\n4 - Atualizar nome\n5 - Sair\n")
    if op == "1":
        print(f"Nome: {conta_1.nome}\nNúmero da conta: {conta_1.numero}\nSaldo: {conta_1.saldo}")
    elif op == "2":
        conta_1.deposito()
    elif op == "3":
        conta_1.saque()
    elif op == "4":
        conta_1.alterarNome()
    elif op == "5":
        break