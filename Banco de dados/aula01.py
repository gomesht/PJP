"""
Create
Read
Update
Delete
"""
import sqlite3


nome = input("Nome do cliente: ")
saldo = float(input("Saldo do cliente: "))
numero = input("Número da conta: ")
agencia = input("Agencia: ")
conexao = sqlite3.connect("bancoDeDados.db")
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'saldo REAL, '
'numero TEXT,'
'agencia TEXT'
')')
cursor.execute('INSERT INTO clientes(nome, saldo, numero, agencia) VALUES (?,?,?,?)',(nome, saldo, numero, agencia))
conexao.commit()
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)

    