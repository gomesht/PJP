comb = input("Deseja abastecer com alcool ou gasolina (a/g): ")
lt = int(input("Quantos litros: "))
#preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
if comb == "g":
    #até 20 litros, desconto de 4% por litro
    #acima de 20 litros, desconto de 6% por litro
    if lt > 20:
        tot = lt * 2.5 * 0.94
    elif lt <= 20:
        tot = lt * 2.5 * 0.96 
    print(f"Valor final: {tot:.2f}")
elif comb == "a":
    #até 20 litros, desconto de 3% por litro
    #acima de 20 litros, desconto de 5% por litro 
    if lt > 20:
        tot = lt * 1.9 * 0.95
    elif lt <= 20:
        tot = lt * 1.9 * 0.97
    print(f"Valor final: {tot:.2f}")
else:
    print("tipo de combustível inválido")