cpf = input("Digite seu CPF: ")
listacpf = []
# ***.***.***-**
if len(cpf) == 14:
    if cpf[3] == cpf[7] and cpf[3] == ".":
        if cpf[11] == "-":
            cpf = cpf.replace(".","")
            cpf = cpf.replace("-","")
            for i in range(12):
                if cpf[i].isnumeric():
                    listacpf.append(int(cpf[i]))
                else:
                    print("CPF invalido")
            print(listacpf)
            mult =0
            for j in range (2,11):
                
                mult += cpf[j]*(10-(j-2))
            divs1 = (mult*10)//11
            res1 = (mult*10)% 11
            mult2=0
            for k in range (2,12):   
                mult2 += listacpf[k]*(11-(k-2))
            divs2 = (mult2*10)//11
            res2 = (mult2*10)% 11
            print(cpf)
           
            if res1 == 10:
                res1 = 0
            if res2 == 10:
                res2 = 0
            print(res1, res2, cpf[9], cpf[10])
            if str(res1) == cpf[9] and str(res2) == cpf[10]:
                print ("CPF válido") 
            else:
                print("CPF inválido")       
        else:
            print("CPF com formato inválido")
    else:
        print("CPF com formato inválido")
else:
    print("CPF incompleto")

                        
            