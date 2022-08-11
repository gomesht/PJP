
while True:
    listac = open('clientes.txt', 'r')
    listap = open('produtos.txt', 'r')


    op = input("Digite o número da opção desejada:\n1 - Adicionar Produto\n2 - Ver Produtos\n3 - Cadastrar Clientes\n4 - Ver Clientes\n5 - Sair\n")
    if op == "5":
        break
    if op == "1":
        
        while True:
            listap = open('produtos.txt', 'r')
            produto = input("Cadastro de produto (digite 0 em produto para voltar):\nNome do produto: ")
            if produto == "0":
                break
            elif listap.read().count(produto) == 0:
                preco = input("Preço do produto: ")
                listap = open('produtos.txt','a')
                listap.write(f"{produto}-{preco}\n")

            else:
                print("Esse produto já foi cadastrado")
            listap.close()
        
    elif op == "2":
        a=0
        while True:
            listap = open('produtos.txt', 'r')
            print(listap.read())
            listap.close()
            a = input("Digite 0 para voltar ")
            if a == "0":
                break
    elif op == "3":
        while True:
            listac = open('clientes.txt', 'r')
            cliente = input("Cadastro de cliente (digite 0 em nome para voltar):\nNome: ")
            if cliente == "0":
                break
            elif listac.read().count(cliente) == 0:
                email = input("Email: ")
                listac = open('clientes.txt','a')
                listac.write(f"{cliente}-{email}\n")
              
            else:
                print("Esse cliente já foi cadastrado")
            listac.close()
    elif op == "4":
        a=0
        while True:
            listac = open('clientes.txt', 'r')
            print(listac.read()) 
            listac.close() 
            a = input("Digite 0 para voltar ")
            if a == "0":
                break
    else:
        print("Digite uma opção válida!")   