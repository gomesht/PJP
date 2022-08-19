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

macacos=[]
while True:
    op = input(f"O que deseja saber ou fazer?\n1 - Criar um novo macaco\n2 - Ver macacos\n3 - Escolher um macaco\n4 - Sair\n")
    if op == "1":
        macacos.append(Macaco(input("Nome do macaco: ")))
    elif op == "2":
        for i in range(len(macacos)):
            print(f"{i} - {macacos[i].nome}")
    elif op == "3":
        i = int(input("informe o numero do macaco: "))
        while True:
            op = input(f"O que deseja saber ou fazer com o macaco {macacos[i].nome}?\n1 - Comer\n2 - Ver o que tem no bucho\n3 - Digerir\n4 - Sair\n")
            if op == "1":
                macacos[i].comer() #Como passar o objeto macaco[i] e não uma string "macaco[i]"
            elif op == "2":
                macacos[i].verBucho()
            elif op == "3":
                macacos[i].digerir()
            elif op == "4":
                break
            else:
                print("Opção inválida")
    elif op == "4":
        break

