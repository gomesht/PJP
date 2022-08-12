#embaralhando sem distinção de palavras

# import random
# def main():
#     palavra = input("Digite uma palavra: ")
#     anagrama = embaralha(palavra)
#     for i in anagrama:
#         print(i,end="")

# def embaralha(a): 
#     mix = []
#     for i in a:
#         mix.append(i)
#     random.shuffle(mix)
#     return mix
# main()

#embaralhando com distinção de palavras
import random
def main():
    texto = input("Digite um texto: ")
    palavras = texto.split(" ")
    for i in palavras:
        anagrama = embaralha(i)
        for j in anagrama:
            print(j,end="")
        print(" ", end="")

def embaralha(a): 
    mix = []
    for i in a:
        mix.append(i)
    random.shuffle(mix)
    return mix
    
main()

