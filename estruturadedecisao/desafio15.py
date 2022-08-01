l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if (l1 + l2) > l3:
    if l1 == l2 and l2 == l3:
        print("É um triângulo equilátero!")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("É um triângulo isóceles!")
    elif l1 != l2 and l2!= l3 and l3 != l1:
        print("É um triângulo escaleno!")
    else:
        print("valores inválidos!")
elif (l1 + l2) <= l3:
    print("Não é um triângulo.")
else:
    ("Valores inválidos")

