"""Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente". """
cl = 0
if input("Telefonou para a vítima (s/n)? ") == "s":
    cl += 1
if input("Esteve no local do crime (s/n)? ") == "s":
    cl += 1
if input("Mora perto da vítima (s/n)? ") == "s":
    cl += 1
if input("Devia para a vítima (s/n)? ") == "s":
    cl += 1
if input("Já trabalhou com a vítima (s/n)? ") == "s":
    cl += 1

if cl == 5:
    print("Assassino")
elif cl >= 3:
    print("Cúmplice")
elif cl >= 2:
    print("Suspeito")
else:
    print("Inocente")
