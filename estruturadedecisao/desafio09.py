num1 = input("Numero 1: ")
num2 = input("Numero 2: ")
num3 = input("Numero 3: ")

maior = num1

if maior < num2:
    maior = num2
if maior < num3:
    maior = num3

menor = num1

if menor > num2:
    menor = num2
if menor > num3:
    menor = num3

medio = num1

if medio == maior or medio == menor :
    medio = num2
if medio == maior or medio == menor :
    medio = num3




print("maior:", maior)
print("meio:", medio)
print("menor:", menor)