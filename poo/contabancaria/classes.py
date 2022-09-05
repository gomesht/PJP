class ContaBancaria:
    def __init__(self, nome, numero, saldo):
        self.__nome = nome
        self.__numero = numero
        self.saldo = float(saldo)
    def __str__(self):
        return f"Conta número: {self.numero} Cliente: {self.nome}\nSaldo: {self.saldo:.2f}"

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    @property
    def numero(self):
        return self.__numero
    def sacar(self, valor):
        if self.saldo > int(valor):
            self.saldo -= int(valor)
        else:
            print(f"Salto insuficiente\nSaldo:{self.saldo:.2f}")
    
    def deposito(self, valor):
        self.saldo += int(valor)
class ContaPoupanca(ContaBancaria):
    def __init__(self, nome, numero, dia, saldo):
        super().__init__(nome, numero, saldo)
        self.dia =  dia
        self.taxa = 1.005
        self.tipo = "poupanca"
    def novo_saldo(self):
        self.saldo =  self.saldo * self.taxa
class ContaEspecial(ContaBancaria):
    def __init__(self, nome, numero, limite, saldo):
        super().__init__(nome, numero, saldo)
        self.limite = limite
    def sacar(self, valor):
        if (self.saldo + float(self.limite)) > int(valor):
            self.saldo  -= int(valor)
        else:
            print(f"Limite insuficiente\nSaldo: {self.saldo}")



    