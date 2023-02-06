#Crie uma classe Funcionario com atributos privados nome, cpf e salário; e um construtor 
#que deve receber como parâmetro nome e cpf. Todos os atributos devem ter métodos 
#getters definidos. Crie métodos setters conforme você sentir necessidade. 
#a. Crie uma classe TrabalhadorAssalariado e outra TrabalhadorHorista, ambas 
#herdando de Funcionario. A classe TrabalhadorAssalariado possui o método 
#definirSalario(salario) que recebe um valor como parâmetro e o atribui ao atributo 
#salário. 
#b. A classe TrabalhadorHorista possui os atributos privados valorHora e 
#horasTrabalhadasMes, com seus respectivos getters e setters. Essa classe também 
#possui o método calcularPagamento(), que ao ser invocado deve calcular o valor do 
#salário e preencher este atributo. O salário é obtido multiplicando-se as horas
#trabalhadas no mês pelo valor da hora. Crie defesas que verifiquem se os atributos 
#necessários para o cálculo do salário estão preenchidos. Se não estiverem emita 
#aviso.

class Funcionario:

    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @property
    def cpf(self):
        return self._cpf

    @nome.setter
    def cpf(self, valor):
        self._cpf = valor
    
    @property
    def salario(self):
        return self._salario

    @nome.setter
    def salario(self, valor):
        self._salario = valor

class TrabalhadorAssalariado(Funcionario):

    def definirSalario(self, salario):
        self._salario = salario
        return self._salario

class TrabalhadorHorista(Funcionario):

    def __init__(self, valorHora, horasTrabalhadasMes):
        self.valorHora = valorHora
        self.horasTrabalhadasMes = horasTrabalhadasMes
    
    @property
    def valorHora(self):
        return self._valorHora

    @valorHora.setter
    def valorHora(self, valor):
        self._valorHora = valor
        
    @property
    def horasTrabalhadasMes(self):
        return self._horasTrabalhadasMes

    @valorHora.setter
    def horasTrabalhadasMes(self, valor):
        self._horasTrabalhadasMes = valor

    def calcularPagamento(self):
        self._salario = self._valorHora * self._horasTrabalhadasMes
        print(self._salario)

vh = int(input('Digite o valor das horas: '))
hrs = int(input('Digite o valor das horas trabalhas: '))
p1 = TrabalhadorHorista(vh, hrs)
p1.calcularPagamento()

    