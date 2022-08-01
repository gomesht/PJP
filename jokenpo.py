import random
c = "s"
ptpc = 0
ptvc = 0
while c == "s":
    pc = random.randint(1,3)
#1 = pedra 2 =  papel 3 = tesoura
    n = input("pedra, papel ou tesoura? ")
    if n == "pedra":
        if pc == 1:
            print("Empate\n")
        elif pc == 2:
            print("Perdeu\n")
            ptpc += 1
        elif pc == 3:
            print("Ganhou\n")
            ptvc += 1

    elif n == "papel":
        if pc == 1:
            print("Ganhou\n")
            ptpc += 1
        elif pc == 2:
            print("Empate\n")
        
        elif pc == 3:
            print("Perdeu\n")
            ptpc += 1
   
    elif n == "tesoura":
        if pc == 1:
            print("Perdeu\n")
            ptpc += 1
        elif pc == 2:
            print("Ganhou\n")
            ptvc += 1
        elif pc == 3:
            print("Empate\n")
    print(f"Placar PC: {ptpc} X Você: {ptvc}\n")
    if ptpc == 3:
        print("\n O PC ganhou")
        c = "n"
    elif ptvc ==3:
        print("\nVocê Ganhou")
        c = "n"
    

    

    