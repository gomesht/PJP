# x = int(input("numero: "))
# match x :
#     case 2:
#         print("dois")
#     case _:
#         print("não é dois")
"""
raça = ''
classe = ''
força = 0
agilidade = 0
inteligência = 0
carisma = 0
guerreiro força +10, agilidade+2 inteligencia+0 carisma
"""
raca = input("Raça: ").lower()
classe = input("Classe: ").lower()
forca = 0
agilidade = 0
inteligencia = 0
carisma = 0

match raca:
    case "humano":
        forca += 4
        agilidade += 3
        inteligencia += 8
        carisma += 6
    case "orc":
        forca += 5
        agilidade += 4
        inteligencia += 2
        carisma += 1
    case "elfo":
        forca += 3
        agilidade += 7
        inteligencia += 9
        carisma += 9
    case "anão":
        forca += 5
        agilidade += 2
        inteligencia += 6
        carisma += 7
    case "gigante":
        forca += 9
        agilidade += 1
        inteligencia += 2
        carisma += 3
    case _ :
        print("Raça inexistente")
match classe:
    case "guerreiro":
        forca += 8
        agilidade += 6
        inteligencia += 1
        carisma += 2
    case "arqueiro":
        forca += 2
        agilidade += 6
        inteligencia += 6
        carisma += 2
    case "gatuno":
        forca += 0
        agilidade += 8
        inteligencia += 9
        carisma += 8
    case "mago":
        forca += 1
        agilidade += 1
        inteligencia += 9
        carisma += 4
    case _ :
        print("Classe inexistente.")

print(f"Raça: {raca}\nClasse: {classe}\nForça: {forca} Agilidade: {agilidade} Inteligência: {inteligencia} Carisma: {carisma}")
        