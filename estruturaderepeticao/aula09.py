# import random
# pares = []
# impares = []
# numeros = []
# for i in range (10):
#     numeros.append(random.randint(1,100))
# print(numeros)

# for j in numeros:
#     if int(j) % 2 != 0:
#         impares.append(j)
#     if int(j) % 2 == 0:
#         pares.append(j)
    
# print(f"Números : {numeros}")
# print(f"Pares : {pares}")
# print(f"Impares : {impares}")


# n = int(input("Quantos numeros deseja adicionar? "))
# lista = []
# for i in range(n):
#     lista.append(int(input(f"Digite o numero {i+1}: ")))
# lista.sort()
# print(lista[0], lista[n-1]) ou lista[-1] ou max(lista) min(lista)


# lista = []
# i=0
# while True:
#     n= input("Digite um numero quando quiser parar aperte enter:")
#     if n == "":
#         break
#     else:
#         lista.append(n)
#         i += 1
# lista.sort()
# print(lista[0], lista[i-1])

# perguntas= ["Telefonou para a vítima (s/n)?", "Esteve no local do crime (s/n)?", "Mora perto da vítima (s/n)?", "Devia para a vítima (s/n)?", "Já trabalhou com a vítima (s/n)?"]
# respostas = []
# for i in range(5):
#     respostas.append(input(perguntas[i]))
# nsim = respostas.count("s")
# if nsim == 5:
#     print("Assassino")
# elif nsim >= 3:
#     print("Cumplice")
# elif nsim == 2:
#     print("Suspeito")
# elif nsim < 2:
#     print("Inocente")
