"""while True:
    n1 = float(input("Digite o primeiro número: "))
    op = input("Escolha a operação (+-*/): ")
    n2 = float(input("Digite o segundo número: "))

    if op == "+":
        r = n1 + n2
    elif op == "-":
        r = n1 - n2
    elif op == "*":
        r = n1 * n2
    elif op == "/":
        r = n1 / n2
    else:
        print("Operador inválido")

    print(f"Resultado {r}")
    if input("deseja continuar (s/n): ") == "n":
        break"""

"""while True:
    op = input("Digite a o peração (a (+-*/) b): ")
    op = op.split(" ")
    print(op)
    n1 = float(op[0])
    n2 = float(op[2])

    if op[1] == "+":
        r = n1 + n2
    elif op[1] == "-":
        r = n1 - n2
    elif op[1] == "*":
        r = n1 * n2
    elif op[1] == "/":
        r = n1 / n2
    else:
        print("Operador inválido")
    
    print(f"Resultado {r}")
    if input("deseja continuar (s/n): ") == "n":
        break"""
        
while True:
    op = input("Digite a o peração: ")
    print(eval(op))
    if input("deseja continuar (s/n): ") == "n":
        break