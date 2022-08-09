while True:
    user = input("Digite um nome de usuário: ")
    if user == "0":
        break
    data = open('usuarios.txt', 'r')
    if data.read().count(user) == 0:

        data = open('usuarios.txt', 'a')
        key = input("Digite uma senha: ")
        if len(key) > 6:

            data.write(f'{user} ')
            data2 = open('senhas.txt', 'a')
            data2.write(f'{key} ')
    else:
        print("O usuário já existe tente outro")

print("\n Autenticação de usuário\n")
u = input("Usuário: ")
k = input("Senha: ")
data = open('usuarios.txt', 'r')
if data.read().count(u) == 1:
    
    data2 = open('senhas.txt', 'r')
    if data2.read().count(k) == 1:
        print("acesso permitido")
    else:
        print("Usuario e/ou senha incorretos")
else:
    print("Usuario e/ou senha incorretos")