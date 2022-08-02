n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
op = input("Qual operação deseja realizar (+-*/)? ")

if op == "+":
    n = n1 + n2
elif op == "-":
    n = n1 - n2
elif op == "*":
    n = n1 * n2
elif op == "/":
    n = n1 / n2

print(f"Resultado = {n}")

if n % 2 == 0:
    print(f"O número {n} é par!")
elif n % 2 != 0:
    print(f"O número {n} é impar!")

    

if n >= 0:
    print(f"O número {n} é positivo!")
elif n < 0:
    print(f"O número {n} é negativo!")



if n % 1 == 0:
    print(f"O numero {n} é inteiro!")
elif n % 1 != 0:
    print(f"O número {n} é decimal!")

