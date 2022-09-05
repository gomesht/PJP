class Motor:
    def __init__(self,numCilindro, potencia) -> None:
        self.numCilindro = numCilindro
        self.potencia = potencia
        self.data = ""
    
    def getdata(self):
        self.data = input("Entrada de dados: ")
        return self.data
    def imprimedata(self):
        print(self.data)
    
    def __str__(self):
        return f"numCilintros: {self.numCilindro} Potência: {self.potencia}"

class Veiculo:
    def __init__(self, peso, velmax, preco):
        self.peso = peso
        self.velmax = velmax
        self.preco = preco
        self.data = ""

    def getdata(self):
        self.data = input("Entrada de dados: ")
        return self.data
    def imprimedata(self):
        print(self.data)

class CarroPasseio(Motor, Veiculo):
    def __init__(self, numCilindro, potencia, peso, velmax, preco, cor, modelo) -> None:
        super().__init__(numCilindro, potencia)
        Veiculo.__init__(self, peso, velmax, preco)
        self.cor = cor
        self.modelo = modelo

class Caminhao(Motor, Veiculo):
    def __init__(self, numCilindro, potencia, peso, velmax, preco, toneladas, alturamax, comprimento) -> None:
        super().__init__(numCilindro, potencia)
        Veiculo.__init__(self, peso, velmax, preco)
        self.toneladas = toneladas
        self.altuuramax = alturamax
        self.comprimento = comprimento
        self.data = ""

    def getdata(self):
        self.data = input("Entrada de dados: ")
        return self.data
    def imprimedata(self):
        print(self.data)
    


    


    
mot = Motor(16, 400)
print(mot)
mot.getdata()
mot.imprimedata()