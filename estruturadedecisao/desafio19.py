num = int(input("Digite um numero: "))
if num > 0 and num < 1000:
    num = str(num)
   
    if len(num) == 3:
        
        centena = num[0]
        centena = int(centena)
        dezena = num[1]
        dezena = int(dezena)
        unidade = num[2]
        unidade = int(unidade)
        if centena > 1:
            tcentena = "centenas"
        elif centena <= 1:
            tcentena = "centena"
        if dezena > 1:
            tdezena = "dezenas"
        elif dezena <= 1:
            tdezena = "dezena"
        if unidade > 1:
            tunidade = "unidades"
        elif unidade <= 1:
            tunidade = "unidade"
        print(f"{num} = {centena} {tcentena}, {dezena} {tdezena} e {unidade} {tunidade}")

    elif len(num) == 2:
        dezena = num[0]
        dezena = int(dezena)
        unidade = num[1]
        unidade = int(unidade)

        if dezena > 1:
            tdezena = "dezenas"
        elif dezena <= 1:
            tdezena = "dezena"
        if unidade > 1:
            tunidade = "unidades"
        elif unidade <= 1:
            tunidade = "unidade"
        print(f"{num} = {dezena} {tdezena} e {unidade} {tunidade}")
    elif len(num) == 1:
        unidade = num
        unidade = int(unidade)

        if unidade > 1:
            tunidade = "unidades"
        elif unidade <= 1:
            tunidade = "unidade"
        print(f"{num} = {unidade} {tunidade}")
