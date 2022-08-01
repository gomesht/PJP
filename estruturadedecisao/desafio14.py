nt1 = float(input("Primeira nota: "))
nt2 = float(input("Segunda nota: "))

md = (nt1+nt2)/2

if 9 <= md <= 10:
    print("APROVADO - A")
elif md >= 7.5:
    print("APROVADO - B")
elif md >= 6:
    print("APROVADO - C")
elif md >= 4:
    print("REPROVADO - D")
elif 0 <= md < 4:
    print("REPROVADO - E")
else:
    print("Valores inválidos!")