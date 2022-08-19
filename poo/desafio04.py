"""Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer,
    crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. """
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def crescer (self):
        self.altura += 0.5
    def envelhecer(self):
        if self.idade < 21:
            self.crescer()
        self.idade += 1
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1

pessoa_1 = Pessoa("Maria", 12, 27, 115)

while True:
    op = input(f"O que deseja saber ou fazer com {pessoa_1.nome}?\n1 - Crescer\n2 - Envelhecer\n3 - Engordar\n4 - Emagrecer\n5 - Dados\n6 - Sair\n")
    if op == "1":
        pessoa_1.crescer()
        print(f"Agora {pessoa_1.nome} mede {pessoa_1.altura} cm")
    elif op == "2":
        pessoa_1.envelhecer()
        print(f"Agora {pessoa_1.nome} tem {pessoa_1.idade} anos")
    elif op == "3":
        pessoa_1.engordar()
        print(f"Agora {pessoa_1.nome} pesa {pessoa_1.peso} kg")
    elif op == "4":
        pessoa_1.emagrecer()
        print(f"Agora {pessoa_1.nome} pesa {pessoa_1.peso} kg")
    elif op == "5":
        print(f"Nome: {pessoa_1.nome}\nIdade: {pessoa_1.idade} anos\nAltura: {pessoa_1.altura} cm\nPeso:  {pessoa_1.peso} kg")
    elif op == "6":
        break
    else:
        pass
