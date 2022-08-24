class Pedido:
    def __init__(self):
        self.valor_total = 0
        self.pedido = []
    def adicionar_item(self, Produto, quantidade):
        self.pedido.append(ItemPedido(Produto, quantidade))
    def obter_total(self):
        for item in self.pedido:
            valor = item.produto.valor
            quant = item.quantidade
            self.valor_total += (quant * valor)
        return print(self.valor_total)
    

class ItemPedido:
    def __init__(self, Produto, quantidade) :
        self.quantidade = quantidade
        self.produto = Produto
       
listaProdutos =[]
class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao
        global listaProdutos
        listaProdutos.append(self)
    def __str__(self):
        return f"{self.codigo}, {self.descricao}"

camisa = Produto("0101", 30, "Blusa de algodão estampada")
bone = Produto("0102", 20, "Boné verde")
calca = Produto("0103", 80, "Calça jeans")
[[1,2,3],2]

pedido1 = Pedido()
pedido1.adicionar_item(calca,3)
print(pedido1.valor_total)
print(pedido1.pedido[0].produto.descricao)
for i in listaProdutos:
    print(i)
print(calca.codigo)


