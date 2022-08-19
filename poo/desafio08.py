"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, 
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o 
conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal? """
class Macaco:
    def __init__(self, nome, bucho = []):
        self.nome = nome
        self.bucho = list(bucho)
    def comer(self):
        self.bucho.append(input(f"O que o {self.nome} comeu?"))
    def verBucho(self):
        print(f"{self.nome} tem no bucho: {self.bucho}")
    def digerir(self):
        self.bucho.clear()

macaco_2 = Macaco("Bob",["maçã","banana"])
macaco_1 = Macaco("George",[macaco_2])
while True:
    op = input(f"O que deseja saber ou fazer com o macaco {macaco_1.nome}?\n1 - Comer\n2 - Ver o que tem no bucho\n3 - Digerir\n4 - Sair\n")
    if op == "1":
        macaco_1.comer()
    elif op == "2":
        macaco_1.verBucho()
        print(macaco_1.bucho[0].bucho)
    elif op == "3":
        macaco_1.digerir()
    elif op == "4":
        break
    else:
        print("Opção inválida")