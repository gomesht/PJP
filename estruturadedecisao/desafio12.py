sal = float(input("Informe o salário por hora: "))
hr = float(input("Informe as horas trabalhadas no mes: "))
salb = sal * hr
if salb > 2500:
    txIr = 0.2
elif salb > 1500:
    txIr = 0.1
elif salb > 900:
    txIr = 0.05
elif salb <= 900:
    txIr = 0.0
ir= salb * txIr
inss = salb * 0.1
fgts = salb *0.11
print(f"Salário Bruto : ({sal:.2f} * {hr:.0f}) : R$ {salb:.2f}")
print(f"(-) IR ({txIr*100:.0f}%) : R$ {ir:.2f}")
print(f"(-) INSS (10%) : R$ {inss:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de descontos : R$ {(ir+inss):.2f}")
print(f"Salário Liquido : R$ {(salb - ir - inss):.2f}")