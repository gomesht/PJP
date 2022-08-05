n = int(input("quantas notas você quer adicionar: "))
i = 0
nota = 0
while i < n:
    nota = nota + int(input("Digite uma nota:"))
    i += 1
print(f"Média = {nota/n:.2f}")
