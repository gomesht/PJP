class Estudante:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor
        
class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor):
        self.__salario = valor
    
class Monitor(Estudante, Funcionario):
    def __init__(self, estudante, salario, disciplina):
        super().__init__(estudante.nome, estudante.matricula)
        Funcionario.__init__(self, estudante.nome , salario)
        self.__disciplina = disciplina
    
    @property
    def disciplina(self):
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, valor):
        self.__disciplina = valor

    def __str__(self) :
        return f"Nome: {self.nome} Matricula: {self.matricula} Salario: {self.salario} Disciplina: {self.disciplina}"

aluno = Estudante("Mario", 2022015)
mo = Monitor(aluno, "400,00", "Qímica Organica")
print(mo)