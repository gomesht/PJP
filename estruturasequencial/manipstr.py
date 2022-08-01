#nome = '          esTou nO joVem PrOGRAmador'
#print(nome)
#print(nome.upper())
#print(nome.lower())
#print(nome.capitalize())
#print(nome.title())
#print(nome.strip())

#x = true
#
#while x == true:
#    idade = int(input("Qual sua idade? "))
#
#    if idade < 18:
#        print("Usuário não pode tirar a carteira.")
#    else:
#        print("Já pode tirar a carteira, meus parabens.")
#        x = false
        
#x = 0
#while True:
#   print(x)
#    x += 1
#    if x == 10000:
#        break

"""print("Cadastro de usuário e senha")
usuario = input("Usuário: ")
senha = input("Senha: ")
print("\nLogin\n")
user = (input("Usuário: "))
key = (input("Senha: "))


while usuario != user or senha != key:
    print("\nUsuário e ou senha incorreto(s) \n")
   
    user = (input("Usuário: "))
    key = (input("Senha: "))


print("\n acesso permitido")"""

"""r = "s"
while r == "s":

    x = input("X é igula a : ")
    y = input("Y é igula a : ")

    if x > y:
        print("X é maior que Y")
    elif x < y:
        print("Y é maior que X")
    elif x = y:
        print("X é igual a Y")
    else:
        print("Opção inválida.")

    r = input("Deseja repetir (s/n): ")"""

sexo = input("Qual seu sexo (m/f): ")
sexo = sexo.strip().lower()
sexo = sexo[0]
if sexo == "m":
    print("Você pode se aposentar com 65 anos.")
elif sexo == "f":
    print("Você pode se aposentar com 60 anos.")
else:
    print("Opção inválida.")
