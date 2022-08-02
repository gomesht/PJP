i=0
pesotot = 0
alttot = 0
pesado = 0
leve = 100000000000000000
alto = 0
baixo = 1000000000000000000
cod1 = 0
cod2 = 0
cod3 = 0
cod4 = 0

while True:
    cod = int(input("Digite o código do cliente: "))
    if cod == 0:
        break
    mt = float(input("Digite sua altura (m): "))
    kg = float(input("Digite seu peso (Kg): "))
    pesotot += kg
    alttot += mt
    if pesado < kg:
        pesado = kg
        cod1 = cod
    if leve > kg:
        leve = kg
        cod2 = cod
    if alto < mt:
        alto = mt
        cod3 = cod
    if baixo > mt:
        baixo = mt
        cod4 = cod
    i += 1


mediaalt = alttot/i
mediapeso = pesotot/i
print(f"A média de altura é {mediaalt} m, a media de peso é {mediapeso}\nO cliente {cod3} é o mais alto com {alto} m\nO cliente {cod4} é o mais baixo com {baixo} m\n ")
print(f"O cliente {cod1} é o mais pesado com {pesado} Kg\nO cliente {cod2} é o mais leve com {leve} Kg")
        
    
    
    
