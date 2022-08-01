import random

pc = random.randint(1,100)
i=0
n = int(input("Adivinhe o numero: "))
while True:
    i += 1
    if i >= 5:
        print("Perdeu!")
        break
    elif n < pc:
        n = int(input("O numero é maior: "))
    elif n > pc:
        n = int(input("O numero é menor: "))
    elif n == pc:
        print("Acertou!!!")
        break
    

