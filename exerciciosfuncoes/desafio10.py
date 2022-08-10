import random

def main():
    pontos = lancadados()
    if pontos == 12 or pontos == 2 or pontos == 3:
        fimdejogo()
    elif pontos == 11 or pontos == 7:
        print("Você é natural")
        ganhou()
    else:
        while True:
            print(f'pontos = {pontos}')
            jogo =  lancadados()
            print(f'dados da rodada: {jogo}')
            if jogo == 7:

                fimdejogo()
                break
            elif jogo == pontos:
                ganhou()
                break

def lancadados():
    dados = random.randint(2,12)
    return dados

def fimdejogo():
    print("Você perdeu =(")

def ganhou():
    print("Você Ganhou!!! =)")


main()