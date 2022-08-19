# import phonenumbers
# from phonenumbers import geocoder, carrier

# PhoneNumber = phonenumbers.parse('+55488988157712')
# Carrier =  carrier.name_for_number(PhoneNumber, 'pt-br')
# Geocode = geocoder.country_name_for_number(PhoneNumber, 'pt-br')

# print(f'Seu numero é da operadora {Carrier} e sua localização é {Geocode}.')


# try:
#     print(x)
# except NameError:
#     print("Variável não definida")
# else:
#     print("estou no else")
# finally:
#     print("estou no finally")

# x = -10
# if x < 0:
#     raise ValueError("O número não pode ser menor que 0")

"""
POO

objeto:
    Celular

Caracteristicas:
    tamnho da tela
    bateria
    memoria 
    camera 
    memoria
    processador

funções:
    fazer ligações
    adicionar ou remover apps
    bater foto
Paradigmas da POO:
    Abstração
    Poliformismo
    Encapsulamento
    Herança
"""
# class Celular:
#     def __init__(self,camera, memoria, bateria, modelo):

#         self.camera = camera
#         self.memoria = memoria
#         self.bateria = bateria
#         self.modelo = modelo
# celular_1 = Celular('50mpx','2gb','3000mah','lg k10')
# celular_2 = Celular('10mpx','500mb','7000mah','Nokia T')

# print(celular_1.camera)
# print(celular_1.memoria)
# print(celular_1.bateria)
# print(celular_1.modelo)

# print(celular_2.camera)
# print(celular_2.memoria)
# print(celular_2.bateria)
# print(celular_2.modelo)

# class Carro:
#     def __init__(self,aro,motor,portas,modelo, marca, velocidademax, ac, direcao, airbag, ano):
#         self.aro = aro
#         self.motor = motor
#         self.portas = portas
#         self.modelo = modelo
#         self.marca = marca
#         self.velocidademax = velocidademax
#         self.ac = ac
#         self.direcao = direcao
#         self.airbag = airbag
#         self.ano = ano

# carro_1 = Carro("aro 15","motor 1.4","4 portas","palio","Fiat","200km/h","ar condicionado","direção hidrualica","2 airbags frontais","2015")

# print(carro_1.modelo)
# print(carro_1.marca)
# print(carro_1.ano)
# print(carro_1.portas)
# print(carro_1.aro)
# print(carro_1.motor)
# print(carro_1.velocidademax)
# print(carro_1.ac)
# print(carro_1.direcao)
# print(carro_1.airbag)

class Usuario:
    def __init__(self, nome, email, idade, senha):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.senha = senha

    def add_user(self):
        return("usuário adicionado com sucesso")
    
usuário_1 = Usuario("Henrique","g@gmail.com","31", "h12345")
print(usuário_1.add_user())

#desenvolver 4, 5, 8