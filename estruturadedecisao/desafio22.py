n = int(input("Digite um número: "))

if n % 2 == 0:
    print(f"O número {n} é par!")
elif n % 2 != 0:
    print(f"O número {n} é impar!")
else:
    print("Valor inválido")