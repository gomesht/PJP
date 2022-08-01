
nome = input("Digite seu nome: ")
while len(nome) <= 3:
    nome = input("O nome deve ter maid de 3 digitos\nDigite seu nome: ")
idade = int(input("Digite sua idade: "))
while idade > 70 or idade < 0:
    idade = input("A idade deve estar entre 0 e 70\nDigite sua idade: ")
salario = float(input("Digite seu salário: "))
while salario <= 0:
    salario = float(input("O salário deve ser maior que 0\nDigite seu salário: "))
sexo = input("Digite seu sexo (m/f): ").lower()
while sexo != "f" and sexo != "m":
    sexo = input("O sexo deve ser 'm' ou 'f'\nDigite seu sexo (m/f): ").lower()
estado = input("Digite seu estado civil(s/c/v/d): ").lower()
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
   estado = input("o estado civil deve ser 's' ou 'c' ou 'v' ou 'd'\nDigite seu estado civil(s/c/v/d): ").lower()
print(f"Nome: {nome}, idade: {idade}, salário: {salario}, sexo: {sexo} e estado civil: {estado}")