area = float(input("Informe a área de pintura em m²: "))
#aumento da área em 10% para cobrir a folga de 10%
area = 1.1*area
rl = 108
rg = 20.6
#Usando só latas
if area % rl == 0 :
    lata = area / rl
else:
    lata = (area // rl) + 1
#Usando só galões
if area % rg == 0 :
    galao = area / rg
else:
    galao = (area // rg) + 1
#Usando latas e galões
if area % rl != 0:
    lt = area // rl
    if ((area % rl) % rg) == 0 :
        gl = (area % rl) / rg
    else:
        gl = ((area % rl) // rg)+1
#Imprimindo os resultados
print(f"Voce precisará de {lata:.0f} lata(s) e o custo será:, {(lata * 80):.0f}")
print(f"Voce precisará de {galao:.0f} galão(ões) e o custo será: {galao * 25:.0f}")
print(f"Voce precisará de {lt:.0f} lata(s) e {gl:.0f} galão(ões) e o custo será: {(lt*80) + (gl * 25):.0f}")