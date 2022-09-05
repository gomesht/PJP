class Humano:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        self.__idade = valor
        
    
class Inseto:
    def __init__(self, nome, venenoso, alado):
        self.__nome = nome
        self.__venenoso = venenoso
        self.__alado = alado
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def venenoso(self):
        return self.__venenoso
    
    @venenoso.setter
    def venenoso(self, valor):
        self.__venenoso = valor

    @property
    def alado(self):
        return self.__alado
    
    @alado.setter
    def alado(self, valor):
        self.__alado = valor
        
    
class SuperHeroi(Humano, Inseto):
    def __init__(self, nome, idade, venenoso, alado, codinome, poderes):
        super().__init__(nome, idade)
        Inseto.__init__(self, nome, venenoso, alado)
        
        self.__codinome = codinome
        self.__poderes  = poderes
    
    @property
    def codinome(self):
        return self.__codinome
    
    @codinome.setter
    def codinome(self, valor):
        self.__codinome = valor

    @property
    def poderes(self):
        return self.__poderes
    
    @poderes.setter
    def poderes(self, valor):
        self.__poderes = valor
    
    def __str__(self):
        return f"Nome: {self.nome} Codinome: {self.codinome} \nIdade: {self.idade} \nVenenoso: {self.venenoso}\nAlado: {self.alado}\nPoderes: {self.poderes}"
    
ha = SuperHeroi("Peter", 20, False, False, "Spider-man", ["sentido aranha","escalar","lançar teia","melhoramento genetico de visão e força"])    
print(ha)


