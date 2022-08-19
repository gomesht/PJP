"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
     Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.""" 
class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def mudarLados(self):
        self.ladoA = int(input("Novo valor do lado A: "))
        self.ladoB = int(input("Novo valor do lado B: "))
    def valorLados(self):
        print(f"Lado A: {self.ladoA} Lado B: {self.ladoB}")
    def area(self):
        print(f"Área: {self.ladoA*self.ladoB}")
    def perimetro(self):
        print(f"Perimetro: {(2*self.ladoA)+(2*self.ladoB)}")
retangulo = Retangulo(4,5)
while True:
    op = input(f"Retângulo:\n1 - Mudar lados\n2 - Valor dos lados\n3 - Área\n4 - Perímetro\n5 - Sair\n")
    if op == "1":
        retangulo.mudarLados()
    elif op == "2":
        retangulo.valorLados()
    elif op == "3":
        retangulo.area()
    elif op == "4":
        retangulo.perimetro()
    elif op == "5":
        break
    else:
        print("Opção inválida")