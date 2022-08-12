import random
palavras = []
with open("palavras.txt") as file:
    for line in file:
        palavras.append(line.rstrip())
random.shuffle(palavras)
forca = palavras[0].lower()
mostra = []
for i in range(len(forca)):
    mostra.append("#")
c = 5
resta =  len(forca)
vida = False
usadas = []
while True:
    
    for i in mostra:
        print(i, end = "")
    print(" ")
    while True:
        tentativa = input(f"Letras usadas {usadas}\nDigite uma letra: ")
        if usadas.count(tentativa) == 0:
            break
        else:
            print("já usada")
    usadas.append(tentativa)
    for i in range(len(forca)):
        if tentativa == forca[i]:
            print(f"a palavra tem '{tentativa}' na posição {i} ")
            mostra[i] = f"{tentativa}" 
            resta -= 1
            vida = True
    print(f"Falta acertar {resta} letra(s).")
    if vida != True:
        c -=1
        vida = False
        print(f"Perdeu uma vida restam {c}") 
    else:
        vida = False
    if c == 0:
        print(f"Palavra : {forca}")
        print("Que pena vôce perdeu!")
        break
    elif resta == 0:
        print("Parabéns! Você acertou!")
        break

      

