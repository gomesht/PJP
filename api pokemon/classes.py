class Pokemon:
    def __init__(self, nome, fig):
        self.nome = nome
        self.fig  = fig    
    def ataque(self):
        return f"roar, scratch"

class Fogo(Pokemon):
    def ataque(self):
        return f"Ember, Fire Fang"
    def eficacia(self):
        return f" Eficaz contra Inseto, Planta, Gelo e Aço\nNão muito eficaz contra Dragão, Pedra e Agua"
    
class Agua(Pokemon):
    def ataque(self):
        return f"Bubble, Splash, Water Gun"
    def eficacia(self):
        return f" Eficaz contra Fogo, Terra e Pedra\nNão muito eficaz contra Dragão, Grama e Aço"
    
class Grama(Pokemon):
    def ataque(self):
        return f"Razor Leaf, Vine Whip"
    def eficacia(self):
        return f" Eficaz contra Agua, Terra, Pedra\nNão muito eficaz contra Inseto, Fogo, Voador, Gelo, Veneno"
    
class Voador(Pokemon):
    def ataque(self):
        return f"Peck, Wing Attack"
    def eficacia(self):
        return f" Eficaz contra Inseto, Planta e Lutador\nNão muito eficaz contra Elétrico, Gelo e Pedra"
    
class Veneno(Pokemon):
    def ataque(self):
        return f"Acid, Poison Jab, Poison sting"
    def eficacia(self):
        return f" Eficaz contra Planta e Fada\nNão muito eficaz contra Solo e Psíquico"
    
class Eletrico(Pokemon):
    def ataque(self):
        return f"Spark, Thunder Shock"
    def eficacia(self):
        return f" Eficaz contra Voador e Agua\nNão muito eficaz contra Dragão Terra e Planta"
    
class Terra(Pokemon):
    def ataque(self):
        return f"Mud Slap"
    def eficacia(self):
        return f" Eficaz contra Elétrico, Veneno, Fogo, Aço e Pedra\nNão muito eficaz contra Gelo, Agua e Planta"
    
class Pedra(Pokemon):
    def ataque(self):
        return f"Rock Trhow"
    def eficacia(self):
        return f" Eficaz contra Inseto, Voador, Fogo e Gelo\nNão muito eficaz contra Lutador, Solo, Agua, Aço e planta"
    




        