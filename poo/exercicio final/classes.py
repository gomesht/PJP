from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.saldo = saldo
        self.agencia = agencia
        self.numero = numero
        self.limite = 0

    @abstractmethod
    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print(f"Saque realizado! Valor sacado: R${valor:.2f}\nNovo saldo: R${self.saldo:.2f}")
        else:
            print(f"Saldo insuficiente!\nSaldo atual: R${self.saldo}")
    def depositar(self,valor):
        self.saldo += valor
        print(f"Novo saldo: R${self.saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite):
        super().__init__(agencia, numero, saldo)
        self.limite = limite
    def sacar(self, valor):
        return super().sacar(valor)

    def criaContaCorrente(self):
        ag = int(input("Agência: "))
        nmr = int(input("Numero: "))
        sld = float(input("Saldo: "))
        lmt = float(input("Limite: "))
        return ContaCorrente(ag, nmr, sld, lmt)

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo)

    def sacar(self, valor):
        return super().sacar(valor)

    def criaContaPoupanca(self):
        ag = int(input("Agência: "))
        nmr = int(input("Numero: "))
        sld = float(input("Saldo: "))
        return ContaPoupanca(ag, nmr, sld)

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    def criarConta(self):
        op = input("Conta corente (c) ou Conta poupança(p): ")
        if op.lower() == "c":
            self.conta = (ContaCorrente.criaContaCorrente(self))
        elif op.lower() == "p":
            self.conta = (ContaPoupanca.criaContaPoupanca(self))
        else:
            print("Opção inválida, tente novamente!")

class Banco:
    def __init__(self):
        self.clientes = []
        self.agencias = []
    
    def addAgencia(self):
        self.agencias.append(int(input("Número da nova agência:")))
    
    def addCliente(self):
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cliente = Cliente(nome, idade)
        cliente.criarConta()
        self.clientes.append(cliente)

    def autenticacao(self):
        altCliente = input("Nome do cliente: ") 
        altConta = input("Número da conta: ")
        altAgencia = input("Número da agência: ")
        c = 0
        for i in range(len(self.clientes)):
            if altCliente == self.clientes[i].nome:
                c += 1
            if int(altConta) == self.clientes[i].conta.numero:
                c += 1

        if int(altAgencia) in self.agencias:
            c += 1
        if c == 3:
            return True
        else:
            return False



bancodobrasil = Banco()
bancodobrasil.addAgencia()
bancodobrasil.addCliente()
print(bancodobrasil.clientes[0].nome)
print(bancodobrasil.clientes[0].idade)
print(bancodobrasil.clientes[0].conta.saldo)
print(bancodobrasil.autenticacao())