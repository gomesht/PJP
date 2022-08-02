tabuada = int(input("Tabuada do número: "))
c = int(input("Começando do número: "))
f = int(input("Até o numero: "))

for i in range(c,f+1):
    print(f"{tabuada} x {i} = {tabuada*i}")