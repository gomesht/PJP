numero = input("Digite seu CPF: ")
cpf = []
validade = []
if len(numero) == 14:
    if numero[3] == "." and numero[7] == "." and numero[11] == "-":
        for i in range (len(numero)):
            cpf.append(numero[i])
        cpf.remove(".")
        cpf.remove(".")
        cpf.remove("-")
        
            
        for i in range(len(cpf)):
            if cpf[i].isnumeric() == True:
                cpf[i]=int(cpf[i])
                validade.append("ok")
            else:
                validade.append("n")
        if validade.count("ok") == 11:
            mult=0
            mult2=0
            for j in range (9):
                mult += cpf[j]*(10-(j))
            res1 = (mult*10)% 11
            for k in range (10):   
                mult2 += cpf[k]*(11-(k))
            res2 = (mult2*10)% 11
            if cpf[0] == cpf[1] and cpf[1]==cpf[2] and cpf[2]==cpf[3] and cpf[3]==cpf[4] and cpf[4]==cpf[5] and cpf[5]==cpf[6] and cpf[6]==cpf[7] and cpf[7]==cpf[8] and cpf[8]==cpf[9] and cpf[9]==cpf[10]:
                print("CPF inválido")
            elif res1 == cpf[-2] and res2 == cpf[-1]:
                print("CPF válido")
        
        else:
            print("CPF inválido")
    else:
        print("CPF inválido")
else:
    print("CPF invalido")
        
        
        
    
        
