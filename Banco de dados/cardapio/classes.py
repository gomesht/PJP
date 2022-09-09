import sqlite3
class Cardapio:
    def verItens(self):
        conexao = sqlite3.connect("dataBase.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        print("Cardápio:")
        print(f'{"ID":>5}{"Nome":>12}{"Preço":>25}')
        for linha in cursor.fetchall():
            print(f"{linha[0]:>5}{linha[1]:>12}{linha[3]:>25}")
            if linha[2] != None:
                print(f"{' ':<45}{linha[2]}")
            else:
                print("")
        cursor.close()
        conexao.close()

    def addItem(self):
        conexao = sqlite3.connect("dataBase.db")
        cursor = conexao.cursor()
        nome = input("Nome do produto: ")
        descricao = input(f"Descrição do {nome}: ")
        preco = float(input(f"Preço do {nome}: "))
    
        cursor.execute('INSERT INTO produtos(nome, descrocao, preco) VALUES(?,?,?)',(nome, descricao, preco))
        cursor.execute("SELECT * FROM produtos")
        print("Cardápio atualizado: ")
        for linha in cursor.fetchall():
            print(linha)
        cursor.close()
        conexao.close()

    def rmItem(self):
        conexao = sqlite3.connect("dataBase.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        print("Cardápio:")
        for linha in cursor.fetchall():
            print(linha)
        op = int(input("Id do item que deseja remover: "))
        cursor.execute(f'DELETE FROM produtos WHERE id = {op}')
        conexao.commit()
        print("Cardápio atualizado: ")
        for linha in cursor.fetchall():
            print(linha)
        cursor.close()
        conexao.close()

    def alterarItem(self):
        conexao = sqlite3.connect("dataBase.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        print("Cardápio:")
        for linha in cursor.fetchall():
            print(linha)
        op = int(input("Id do item que deseja alterar: "))
        op2 = int(input("O que deseja alterar:\n1 - Nome\n2 - Descrição\n3 - Preço"))
        match op2:
            case 1:
                nome =  input("Novo nome: ")
                cursor.execute(f'UPDATE produtos SET nome = ? WHERE id = {op}',(nome,))
                conexao.commit()
            case 2:
                descricao = input("Nova descrição: ")
                cursor.execute(f'UPDATE produtos SET descricao = ? WHERE id = {op}',(descricao,))
                conexao.commit()
            case 3:
                preco = float(input("Novo preço: "))
                cursor.execute(f'UPDATE produtos SET preco = ? WHERE id = {op}',(preco,))
                conexao.commit()
        cursor.close()
        conexao.close()
    