from classes import Carro
def main():
    consumo = float(input("Consumo do carro em Km/L: "))
    carro1 = Carro(consumo)
    while True:
        op = input("1 - Dirigir\n2 - Mostrar nível de combustível\n3 - Abastecer\n4 - Sair\n")
        match op:
            case "1":
                d = float(input("Quantos Km deseja dirigir: "))
                carro1.andar(d)
            case "2":
                print(carro1.obterGasolina())
            case "3":
                l = float(input("Quantos litros de gasolina vai abastecer: "))
                carro1.addGasolina(l)
            case "4":
                break
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    main()