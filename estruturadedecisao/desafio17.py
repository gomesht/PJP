ano = int(input("Digite o ano: "))
if (ano % 4) == 0:
    print(f"O ano {ano} é bissexto!")
elif (ano % 4) != 0:
    print(f"O ano {ano} não é bissexto!")
else:
    print("Valor inválido!")