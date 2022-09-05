"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso"""
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivel = 0
    def andar(self, dist):
        if dist/self.consumo <= self.nivel:
            print(f"Você andou {dist:.2f} km")
            self.nivel -= (dist/self.consumo)
            print(self.obterGasolina())
        else:
            print("Você não tem gasolina suficiente para esse trajeto\n Abasteça!")
    def obterGasolina(self):
        return(f"Você tem {self.nivel:.2f} litros de gasolina")
    def addGasolina(self, valor):
        self.nivel += valor
        print(self.obterGasolina())

        