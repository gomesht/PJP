a = float(input("Digite o valor de a: "))
if a != 0:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b ** 2) -  (4 * a * c)

    
    if delta == 0:
        raiz1 = -b / 2 * a
        print(f"A equação tem apenas 1 raiz = {raiz1}")
    elif delta > 0:
        raiz1 = (-b + (delta ** (1 / 2))) / 2 * a
        raiz2 = (-b - (delta ** (1 / 2))) / 2 * a
        print(f"A equação tem duas raizes x' ={raiz1} e x'' = {raiz2}")
    elif delta < 0:
        print("A equação não tem raizes reais.")
elif a == 0:
    print("A equação não é do segundo grau.")