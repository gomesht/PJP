
from abc import ABC, abstractmethod
from math import pi
from random import triangular
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado**2
    
    def perimetro(self):
        return self.lado*4
class Triangulo(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado*((3**(1/2))*(self.lado/2))/2
    def perimetro(self):
        return self.lado*3

        
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return pi*(self.raio**2)
    def perimetro(self):
        return pi*self.raio*2
    
class Pentagono(FormaGeometrica):
    def __init__(self, lado) -> None:
        self.lado = lado
    
    def area(self):
        return (5/2)*self.lado*((3**(1/2))*(self.lado/2))
    def perimetro(self):
        return self.lado*5

l = int(input("Lado/Raio:"))

quadrado = Quadrado(l)
print(f"Quadrado de lado {l}:")
print(f"Área: {quadrado.area()}")
print(f"Perimetro: {quadrado.perimetro()}")

triangulo = Triangulo(l)
print(f"Triangulo equilatero de lado {l}:")
print(f"Área: {triangulo.area():.2f}")
print(f"Perimetro: {triangulo.perimetro()}")

circulo = Circulo(l)
print(f"Circulo de raio {l}:")
print(f"Área: {circulo.area():.2f}")
print(f"Perimetro: {circulo.perimetro():.2f}")

pentagono = Pentagono(l)
print(f"Pentagono regular de lado {l}:")
print(f"{pentagono.area():.2f}")
print(pentagono.perimetro())
