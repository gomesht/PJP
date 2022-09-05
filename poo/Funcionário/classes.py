class Funcionario:
    def __init__(self, nome, salario):
        self.nome = str(nome)
        self.salario = float(salario)
    
    def retornar_nome(self):
        return(self.nome)
    
    def retornar_salario(self):
        return(self.salario)
    
    def aumento_salario(self, taxa):
        self.salario += (self.salario * taxa / 100)
        return self.salario