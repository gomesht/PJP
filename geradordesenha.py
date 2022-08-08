import random
lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z","0","1","2","3","4","5","6","7","8","9","+","-","*","/","?","!","@","#","$","%","&","(","(","|","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","W","Y","Z"]
senha = []
n = int(input("Senha de quantos caracteres: "))
tlista = len(lista)-1
for i in range(n):
    caracter = random.randint(0,tlista)
    senha.append(lista[caracter])
print("Senha: ",end="")
for i in range(n):
    print(senha[i], end="")
    
    #import randon e import string