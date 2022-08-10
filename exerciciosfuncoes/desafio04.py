def positivo(a):
    if a >= 0:
        return("P")
    elif a < 0:
        return("N")
n = int(input("Número: "))
print(positivo(n))