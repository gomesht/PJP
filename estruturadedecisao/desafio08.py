p1 = float(input("Produto 1 preço: "))
p2 = float(input("Produto 2 preço: "))
p3 = float(input("Produto 3 preço: "))

barato = p1
p = 1

if barato > p2:
    barato = p2
    p = 2
if barato > p3:
    barato = p3
    p = 3

print("Você deve comprar o ",p,"º produto no valor de", barato)