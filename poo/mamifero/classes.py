from abc import ABC, abstractmethod


class Mamifero(ABC):
    def __init__(self, nome, peso, habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat
    
    def __str__(self) :
        return f"Nome: {self.nome}\nPeso: {self.peso} kg\nHabitat: {self.habitat}"
        
    @abstractmethod
    def fala(self, animal):
        pass

    @abstractmethod
    def locomove(self):
        return f"{self.nome} caminha sobre 4 patas pela {self.habitat}"

    @abstractmethod
    def comer(self, alimento):
        return f"{self.nome} come {alimento}"
        
class Macaco(Mamifero):
    def __init__(self, nome, peso, habitat):
        super().__init__(nome, peso, habitat)
             
    def fala(self, animal):
        return f"{self.nome} se comunica por urros com {animal.nome}"
    def locomove(self):
        return f"{self.nome} pula de galho em galho pela {self.habitat}"
    def comer(self, alimento):
        return super().comer(alimento)

class Cachorro(Mamifero):
    def __init__(self, nome, peso, habitat):
        super().__init__(nome, peso, habitat)
    
    def fala(self, animal):
        return f"{self.nome} se comunica por latidos com {animal.nome}"
    
    def locomove(self):
        return super().locomove()

    def comer(self, alimento):
        return super().comer(alimento)
    
class Gato(Mamifero):
    def __init__(self, nome, peso, habitat):
        super().__init__(nome, peso, habitat)
    
    def fala(self, animal):
        return f"{self.nome} se comunica por miados com {animal.nome}"

    def locomove(self):
        return super().locomove()
    
    def comer(self, alimento):
        return super().comer(alimento)
    
class Baleia(Mamifero):
    def __init__(self, nome, peso, habitat):
        super().__init__(nome, peso, habitat)
    
    def fala(self, animal):
        return f"{self.nome} se comunica por ondas sonoras com {animal.nome}"
    
    def locomove(self):
        return f"{self.nome} nada pelo {self.habitat}"

    def comer(self, alimento):
        return super().comer(alimento)

mcc = Macaco("George",50, "selva")
dog = Cachorro("Marley",35, "cidade")
cat = Gato("Garfield", 12, "cidade")
bla =  Baleia("Willy", 2000, "mar")

print(f"{mcc}\n{mcc.fala(dog)}\n{mcc.comer('Banana')}\n{mcc.locomove()}\n")

print(f"{dog}\n{dog.fala(cat)}\n{dog.comer('Osso')}\n{dog.locomove()}\n")

print(f"{cat}\n{cat.fala(bla)}\n{cat.comer('Banana')}\n{cat.locomove()}\n")

print(f"{bla}\n{bla.fala(mcc)}\n{bla.comer('Planctons')}\n{bla.locomove()}\n")

        
    