class ContaInvestimento:
    def __init__(self, saldo, taxa):
        self.saldo = saldo
        self.taxa = taxa

    def adicionarJuros(self):
        self.saldo += (self.saldo * (self.taxa/100))

    def __str__(self):
        return f"Saldo = R$ {self.saldo:.2f}"
