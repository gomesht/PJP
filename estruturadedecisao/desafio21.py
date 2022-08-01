saque = int(input("Caixa Eletrônico\n Informe o valor do saque: "))
if saque >= 10 and saque <=600:
    resto = saque
    nCem = 0
    nCinquenta = 0
    nDez = 0
    nCinco = 0
    nUm = 0
    if resto >= 100:
        nCem = resto // 100
        resto = resto % 100
    if resto >= 50:
        nCinquenta = resto // 50
        resto = resto % 50
    if resto >= 10:
        nDez = resto // 10
        resto = resto % 10
    if resto >= 5:
        nCinco == resto // 5
        resto = resto % 5
    if resto >= 1:
        nUm == resto
    #if nCem != 0:
    print(f"Notas de 100 = {nCem}")
    #if nCinquenta != 0:
    print(f"Notas de 50 = {nCinquenta}")
    #if nDez !=0:
    print(f"Notas de 10 = {nDez}")
    #if nCinco != 0:
    print(f"Notas de 5 = {nCinco}")
    #if nUm != 0:
    print(f"Notas de 1 = {nUm}")