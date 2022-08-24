from pessoa import Pessoa
pessoa = Pessoa("Rick",50,35,70,100)
print(pessoa)
pessoa.perder_fome()
pessoa.correr()
pessoa.dano()
pessoa.feitico()
print(pessoa)
pessoa.dormir()
pessoa.comer()
print(pessoa)


def patrono():
    for i in range(20):
        pessoa.feitico()
    print("Patrono")

patrono()
print(pessoa)