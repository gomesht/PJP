n = float(input("Digite um número: "))

if n % 1 == 0:
    print(f"O numero {n} é inteiro!")
elif n % 1 != 0:
    print(f"O número {n} é decimal!")
else:
    print("Valor inválido")

