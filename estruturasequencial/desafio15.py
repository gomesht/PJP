val = float(input("Informe seu salário por hora: "))
horas = float(input("Informe as horas trabalhadas esse mês:"))
sal = val*horas
print("+ Salário Bruto : R$", sal)
print("- IR (11%) : R$", sal*.11)
print("- INSS (8%) : R$", sal*.08)
print("- Sindicato (5%) : R$", sal*.05)
print("Salário Liquido : R$", sal*.76)
