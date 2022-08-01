sal = float(input("Digite seu salário: "))
a="ok"
if sal > 1500:
    fator = 0.05
elif sal > 700:
    fator = 0.1
elif sal > 280:
    fator = 0.15
elif 0 < sal <= 280:
    fator = 0.2
else:
    print("Valor inválido.")
    a = "nok"
if a == "ok":
    print(f"Salario anterior: {sal}\n Percentual de aumento: {fator*100}%\nSalário atualizado: {sal*(1+fator)}")