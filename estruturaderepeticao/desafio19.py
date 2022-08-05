votos = []
while True:
   
    v = input("Vote no melhor Sistema Operacional para uso em servidores:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n")
    if v == "0":
        break
   # elif v =="1" or v =="2" or v =="3" or v =="4" or v =="5" or v =="6":
    elif v > "0" and v <= "6":
        votos.append(int(v))
    else:
        print("Digite um inteiro de 0 a 6")

v1 = votos.count(1)
v2 = votos.count(2)
v3 = votos.count(3)
v4 = votos.count(4)
v5 = votos.count(5)
v6 = votos.count(6) 
qtv = len(votos)
p1 = v1*100/qtv
p2 = v2*100/qtv
p3 = v3*100/qtv
p4 = v4*100/qtv
p5 = v5*100/qtv
p6 = v6*100/qtv

print("Sistema operacional - Votos - %")
print(f"Windows server - {v1} - {p1:.2f} %")
print(f"Unix - {v2} - {p2:.2f} %")
print(f"Linux - {v3} - {p3:.2f} %")
print(f"Netware - {v4} - {p4:.2f} %")
print(f"Mac OS - {v5} - {p5:.2f} %")
print(f"Outro - {v6} - {p6:.2f} %")
print(f"Total de votos = {qtv}")