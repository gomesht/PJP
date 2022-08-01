num1 = input("Numero 1: ")
num2 = input("Numero 2: ")
num3 = input("Numero 3: ")

maior = num1

if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
print("maior:", maior)
