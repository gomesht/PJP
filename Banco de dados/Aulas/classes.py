import sqlite3
from validacaoCPF import validarCpf
class Agenda:
    def verItens(self):
        conexao = sqlite3.connect("bancoAgenda.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agenda")
        print("Agenda:")
        print(f'{"ID":>5}{"Nome":>12}{"Telefone":>12}{"Endereço":>20}{"CPF":>15}')
        for linha in cursor.fetchall():
            print(linha)
            #f"{linha[0]:>5}{linha[1]:>12}{linha[2]:>12}{linha[3]:>20}{linha[4]:>15}"
            
        cursor.close()
        conexao.close()

    def addItem(self):
        conexao = sqlite3.connect("bancoAgenda.db")
        cursor = conexao.cursor()
        nome = input("Nome do contato: ")
        telefone = int(input(f"Telefone de {nome}: "))
        preco = input(f"Endereço de {nome}: ")
        cpf = input(f"CPF de {nome}: ")
        while True:
            if validarCpf(cpf) == True:
                cpf = float(cpf)
                break
            else:
                cpf = float(input(f"CPF de {nome}: "))
    
        cursor.execute('INSERT INTO agenda(nome, telefone, endereco, cpf) VALUES(?,?,?,?)',(nome, telefone, preco, cpf))
        cursor.execute("SELECT * FROM agenda")
        print("Agenda atualizada: ")
        for linha in cursor.fetchall():
            print(linha)
        cursor.close()
        conexao.close()

    def rmItem(self):
        conexao = sqlite3.connect("bancoAgenda.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agenda")
        print("Agenda:")
        for linha in cursor.fetchall():
            print(linha)
        op = int(input("Id do contato que deseja remover: "))
        cursor.execute(f'DELETE FROM agenda WHERE id = {op}')
        conexao.commit()
        print("Agenda atualizada: ")
        for linha in cursor.fetchall():
            print(linha)
        cursor.close()
        conexao.close()

    def alterarItem(self):
        conexao = sqlite3.connect("bancoAgenda.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agenda")
        print("Agenda:")
        for linha in cursor.fetchall():
            print(linha)
        op = int(input("Id do contato que deseja alterar: "))
        op2 = int(input("O que deseja alterar:\n1 - Nome\n2 - Telefone\n3 - Endereço\n4 - CPF"))
        match op2:
            case 1:
                nome =  input("Novo nome: ")
                cursor.execute(f'UPDATE agenda SET nome = ? WHERE id = {op}',(nome,))
                conexao.commit()
            case 2:
                telefone = input("Novo telefone: ")
                cursor.execute(f'UPDATE agenda SET telefone = ? WHERE id = {op}',(telefone,))
                conexao.commit()
            case 3:
                endereco = float(input("Novo endereço: "))
                cursor.execute(f'UPDATE agenda SET endereco = ? WHERE id = {op}',(endereco,))
                conexao.commit()
            case 4:
        
                cpf = float(input("Novo CPF: "))
                while True:
                    valid = validarCpf(str(cpf))
                    if valid == True:
                        break
                    else:
                        cpf = float(input("Novo CPF: "))
                cursor.execute(f'UPDATE agenda SET cpf = ? WHERE id = {op}',(cpf,))
                conexao.commit()
        cursor.close()
        conexao.close()