nome = input("Nome do piloto: ")
vel = 0
maxvel = 0
horas = 0
def main():
    while True:
        op = input("O que deseja fazer:\n1 - Acelerar\n2 - Desacelerar\n3 - Informações\n4 - Parar Carro:\n")
        if op == "1":
            acelerar_carro()
        elif op == "2":
            desacelerar_carro()
        elif op == "3":
            informacoes()
        elif op == "4":
            finalizar()
            break

def acelerar_carro():
    global vel, horas, maxvel
    if vel < 100:
        vel += 5
    elif vel == 100:
        print("Você está muito rápido redzindo a velocidade para 95 km/h")
        vel -= 5
    horas += 1
    if vel > maxvel:
        maxvel = vel
def desacelerar_carro():
    global vel, horas
    vel -= 5
    if vel <= 0:
        print("O carro está parado")
        vel = 0
    horas += 1
def informacoes():
    global nome, horas, vel
    print(f"Nome do piloto: {nome}\nVelocidade atual: {vel} km/hr\nTempo de corrida: {horas} hrs")
def finalizar():
    global vel, horas, maxvel
    print(f"Corrida finalizada\nDuração da corrida: {horas} hrs\nVelocidade máxima: {maxvel} km/h")

main()
