import sqlite3

conexao = sqlite3.connect("bancodedados.db")
cursor = conexao.cursor()
print("Peso acima de 60 kg")
cursor.execute("SELECT * FROM pessoas WHERE peso > 60")
for linha in cursor.fetchall():
        print(linha)
print("Sexo feminino")
cursor.execute("SELECT * FROM pessoas WHERE sexo = 'feminino'")
for linha in cursor.fetchall():
        print(linha)
print("Classe alta")
cursor.execute("SELECT * FROM pessoas WHERE CLASSE = 'alta'")
for linha in cursor.fetchall():

        print(linha)

print("Sexo feminino, peso acima de 60, maior de 18, classe alta")
cursor.execute("SELECT * FROM pessoas WHERE sexo = 'feminino' AND peso > 60 AND classe = 'media' AND idade > 18")
for linha in cursor.fetchall():
    
        print(linha)

cursor.execute('UPDATE pessoas SET (peso, classe) = (?,?) WHERE idade > 60',(98, "media"))
conexao.commit()

cursor.execute("SELECT * FROM pessoas")
for linha in cursor.fetchall():

    print(linha)


cursor.execute("SELECT * FROM pessoas WHERE idade > 60")
for linha in cursor.fetchall():
        print(linha)

cursor.close()
conexao.close()