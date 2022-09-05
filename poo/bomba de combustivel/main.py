from classes import BombaCombustivel
def main():
    tipo = input("Abrindo Posto\nInforme o tipo de combustivel vendido: ")
    valor = float(input(f"Informe o valor do litro de {tipo}: "))
    quant = float(input("Informe quanto combustível está disponivel: "))
    posto = BombaCombustivel(tipo,valor,quant)
    while True:
        op = input("Posto de Combustível:\n1 - Abastecer por valor\n2 - Abastecer por litros\n3 - Mudar combustível\n4 - Mudar valor do litro\n5 - Mudar quantidade de combustível\n6 - Fechar\n")
        match op:
            case "1":
                vl = float(input("Qual valor deseja abastecer? "))
                posto.abastecer_valor(vl)
            case "2":
                lt = float(input("Quantos litros deseja abastecer? "))
                posto.abastecer_litro(lt)
            case "3":
                tp = input("Mudar para qual combustivel? ")
                posto.alterar_combustivel(tp)
            case "4":
                vl = float(input("Qual o novo valor do litro? "))
                posto.alterar_valor(vl)
            case "5":
                qt = float(input("Qual a nova quantidade de combustível? "))
                posto.alterar_quantidade(qt)
            case "6":
                break
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
