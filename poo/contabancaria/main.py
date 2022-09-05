from classes import ContaBancaria, ContaEspecial, ContaPoupanca
def main():
    dados = []
    while True:
        op = input("Banco Python:\n1 - Cadastro de cliente\n2 - Sacar de alguma conta\n3 - Depositar em alguma conta\n4 - Mostrar novo saldo de uma conta Poupança\n5 - Mostrar dados de uma conta\n6 - Sair\n")
        match op:
            case "1":
                op = input("Escolha o tipo de conta:\n1 - Conta Bancaria\n2 - Conta Poupança\n3 - Conta Especial\n")
                match op:
                    case "1":
                        
                        nome  = input("Nome: ")
                        while True:
                            numero = input("Numero: ")
                            vn = 0
                            for i in dados:
                                if i.numero == numero:
                                    print("Número inválido")
                                    vn += 1
                            if vn == 0:
                                break

                        saldo = input("Saldo: ")
                        dados.append(ContaBancaria(nome, numero, saldo))
                    case "2":
                        nome  = input("Nome: ")
                        while True:
                            numero = input("Numero: ")
                            vn = 0
                            for i in dados:
                                if i.numero == numero:
                                    print("Número inválido")
                                    vn += 1
                            if vn == 0:
                                break
                        saldo = input("Saldo: ")
                        dia = input("Dia: ")
                        dados.append(ContaPoupanca(nome, numero, saldo, dia))
                    case "3":
                        nome  = input("Nome: ")
                        while True:
                            numero = input("Numero: ")
                            vn = 0
                            for i in dados:
                                if i.numero == numero:
                                    print("Número inválido")
                                    vn += 1
                            if vn == 0:
                                break
                        saldo = input("Saldo: ")
                        limite = input("Limite: ")
                        dados.append(ContaEspecial(nome, numero, saldo, limite))    
                    case _:
                        print("Opção inválida!")                    
                        
            case "2":
                n = input("Numero da conta: ")
                v = input("Valor do saque: ")
                vop = 0
                for i in dados:
                    if i.numero == n:
                        i.sacar(v)
                        print(i)
                        vop += 1
                if vop == 0:
                    print("Falha na operação número da conta inexistente!")
            case "3":
                n = input("Numero da conta: ")
                v = input("Valor do depósito: ")
                vop = 0
                for i in dados:
                    if i.numero == n:
                        i.deposito(v)
                        print(i) 
                        vop += 1
                if vop == 0:
                    print("Falha na operação número da conta inexistente!")

            case "4":
                n = input("Numero da conta: ")
                try:
                    for i in dados:
                        if i.numero == n:
                            i.novo_saldo()
                            print(i)
                except AttributeError:
                    print("Essa não é uma conta poupança!")
            case "5":
                n = input("Numero da conta: ")
                for i in dados:
                    if i.numero == n:
                        print(i)
            case "6":
                break
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()