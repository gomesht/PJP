# import sqlite3
# conexao = sqlite3.connect("dataBase.db")
# cursor = conexao.cursor()

# cursor.execute('DELETE FROM clientes WHERE peso > 100 OR peso < 50')
# conexao.commit()
# nomes = []
# cursor.execute("SELECT * FROM clientes")
# for linha in cursor.fetchall():
#     if linha[1] not in nomes:
#         nomes.append(linha[1])
        
# for nome in nomes:
#     cursor.execute(f"SELECT * FROM clientes WHERE nome = '{nome}'")
#     ids = []
#     for linha in cursor.fetchall():
#         print(linha)
        
#         ids.append(linha[0])
#     op = 0
#     while True:
#         if op not in ids:
#             op = int(input("Escolha o ID do cliente que deseja manter: "))
#         else:
#             ids.remove(op)
#             break
#     print(ids)
#     for id in ids:
#         cursor.execute(f'DELETE FROM clientes WHERE id = {id}')
#         conexao.commit()

# cursor.execute("SELECT * FROM clientes")
# for linha in cursor.fetchall():
#     print(linha)
# print(f"\nFIM\n")

# import sqlite3
# conexao = sqlite3.connect("dataBase2.db")
# cursor = conexao.cursor()
# cursor.execute("SELECT * FROM clientes")
# for linha in cursor.fetchall():
#     print(linha)
# print("\n")
# cursor.execute('DELETE FROM clientes WHERE mensalidade = 0')
# conexao.commit()
# print("Clientes adimplentes")
# cursor.execute("SELECT * FROM clientes")
# for linha in cursor.fetchall():
#     print(linha)
