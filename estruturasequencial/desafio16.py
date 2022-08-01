area = int(input("Informe a área de pintura em m²: "))
if area % 54 == 0 :
    lata = area / 54
else:
    lata = (area // 54) + 1

print("Voce precisará de ", lata," lata(s) e o custo será: ", lata * 80)