"""def soma(numero): # <- Parametro (numero = 10) <- padrão se não houver entrada
    print(f"Estou somando o numero {numero}")

soma(2) #<- Argumento"""
"""def nome_usuario(nome, idade):
    print(f"o nome do usuário é {nome} e a sua idade é {idade}.")
    return (f"o nome do usuário é {nome} e a sua idade é {idade}.")
username = str(input("Qual seu nome: "))
userage = int(input("Qual sua idade: "))
print(nome_usuario(username, userage).upper())"""


#classes:

# listas = ["1","2"]
# sets = {"1","2","3","4","5"}
# dicionarios = {id:"valor"}
# tuplas = ("1","2") # não pode alterar valores, remover, adicionar. Um unico valor sem vírgula retorna o valor específico 
#complexos =
#for i in tuplas:
# print(tuplas)
# print(list(tuplas))
# tuplas = list(tuplas)
# print(tuplas)

# def x (*arg):
#     print(arg)
# x(1,2,3,4,5) <- (1,2,3,4,5)

# def x (*arg):
#     print(*arg)
# x(1,2,3,4,5) <- 1 2 3 4 5

# def x (**kwargs):
#     print(kwargs)

# x(veiculo = 'carro', portas = 4, velmax = 300)

# def is_prime(number):
#     c = 0
#     for i in range(1,number+1):
#         if number % i == 0:
#             c += 1
#     if c == 2:
#         return True
#     else:
#         return False

# """Criar uma função que verifica se um número é primo """
# n = int(input("Número: "))
# print(is_prime(n))
# primos = []
# for i in range (1,9999):
#     if is_prime(i) == True:
#         primos.append(i)
#     i += 1
# print(primos)

# def is_prime(number):
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     if number < 2:
#         return False
#     return True
# primos = []
# for i in range (1,999999):
#     if is_prime(i) == True:
#         primos.append(i)
#     i += 1
# print(primos)