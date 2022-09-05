from classes import ContaInvestimento
def main():
    saldo = float(input("Saldo investido: "))
    taxa = float(input("Taxa de rendimento em %: "))
    meses = int(input("Quantos meses o dinheiro ficará investido: "))
    conta = ContaInvestimento(saldo,taxa)
    for i in range(meses):
        conta.adicionarJuros()
    print(conta)
if __name__ == "__main__":
    main()