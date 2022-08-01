nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = float((nota1 + nota2)/2)
if media == 10:
    print("Aprovado com Distinção")
elif 7 <= media < 10:
    print("Aprovado")
elif 0 < media < 7:
    print("Reprovado")
else:
    print("Notas inválidas.")

