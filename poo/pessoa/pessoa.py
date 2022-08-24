
class Pessoa:

    def __init__(self, nome, fomem, manam, energiam, vidam):
        self.__nome = nome
        self.__fome = fomem
        self.__mana = manam
        self.__energia = energiam
        self.__vida = vidam
        self.__fomem = fomem
        self.__manam = manam
        self.__energiam = energiam
        self.__vidam = vidam
    def __str__(self):
        return f"Nome: {self.nome}\nVida: {self.vida}\nEnergia: {self.energia}\nFome: {self.fome}\nMana: {self.mana}"

    @property
    def nome(self):
        return self.__nome

    @property
    def fome(self):
        return self.__fome
    @fome.setter
    def fome(self,valor):
        self.__fome = valor

    @property
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self, valor):
        self.__mana = valor

    @property
    def energia(self):
        return self.__energia
    @energia.setter
    def energia(self, valor):
        self.__energia = valor

    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, valor):
        self.__vida = valor


    @property
    def fomem(self):
        return self.__fomem
    @fomem.setter
    def fomem(self,valor):
        self.__fomem = valor

    @property
    def manam(self):
        return self.__manam
    @manam.setter
    def manam(self, valor):
        self.__manam = valor

    @property
    def energiam(self):
        return self.__energiam
    @energiam.setter
    def energiam(self, valor):
        self.__energiam = valor

    @property
    def vidam(self):
        return self.__vidam
    @vidam.setter
    def vidam(self, valor):
        self.__vidam = valor
    
    def perder_fome(self):
        self.fome -= 1
    
    def comer(self):
        self.fome += 1
    
    def correr(self):
        self.energia -= 1
        self.fome -= 1
    
    def dormir(self):
        self.energia = self.energiam
        self.mana = self.manam
        self.vida = self.vidam

    def feitico(self):
        self.mana -= 1

    def dano(self):
        self.vida -= 1






