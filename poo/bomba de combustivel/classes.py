class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_litro(self, valor):
        if valor <= self.quantidade_combustivel:
            self.alterar_quantidade(-valor)
            print(f"Você abasteceu {valor} litros de {self.tipo_combustivel}  valor = {valor * self.valor_litro:.2f}")
        else:
            print("Desculpe não temos combustível insuficiente!")

    def abastecer_valor(self, valor):
        if (valor/self.valor_litro) <= self.quantidade_combustivel:
            self.alterar_quantidade(-valor)
            print(f"Você abasteceu {valor/self.valor_litro:.2f} litros de {self.tipo_combustivel}  valor = {valor}")
        else:
            print("Desculpe não temos combustível insuficiente!")

    def alterar_valor(self, valor):
        self.valor_litro = valor
        
    def alterar_combustivel(self, valor):
        self.tipo_combustivel = valor

    def alterar_quantidade(self, valor):
        self.quantidade_combustivel += valor