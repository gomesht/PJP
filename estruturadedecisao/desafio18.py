data = input("Informe uma data (dd/mm/aaaa): ")
data =  data.split("/")


dia = int(data[0])
mes = int(data[1])


if dia > 0 and dia <= 31:
    if mes > 0  and mes <=12:
        if len(data[2]) == 4:
            if len(data[1]) == 2:
                print("data válida!")
            else:
                print("data inválida!")
        else:
            print("data inválida!")
    else:
        print("data inválida!")
else:
    print("data inválida!")
    """elif mes == 2:
        if 0 > dia > 30:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 3:
        if 0 > dia > 32:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 4:
        if 0 > dia > 31:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 5:
        if 0 > dia > 32:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 6:
        if 0 > dia > 31:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 7:
        if 0 > dia > 32:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 8:
        if 0 > dia > 32:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 9:
        if 0 > dia > 31:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 10:
        if 0 > dia > 32:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 11:
        if 0 > dia > 31:
            if len(ano) == 4:
                print("data válida!")
    elif mes == 12:
        if 0 > dia > 32:
            if len(ano) == 4:
                print("data válida!")"""
    

