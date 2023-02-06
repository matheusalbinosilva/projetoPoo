class Funcionario:
    
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento
    
    def bonificar(self):
        aumento = (self.salario / 100 * 10) + self.salario
        print(aumento)
        
        
class Gerente(Funcionario):

    def __init__(self, senha, numero_funcionarios, salario_gerente):
        self.senha = senha
        self.numero_funcionarios = numero_funcionarios
        self.salario_gerente = salario_gerente

    def autenticarSenha(self, senha,):
        if self.senha == senha:
            return 'True'
            
        else:
            return 'False'

    def bonificar(self):
        aumento_gerente = (self.salario_gerente / 100 * 15) + self.salario_gerente
        print(aumento_gerente)


funcionario1 = Funcionario('Carlos', 11456474185, 2000, 'Rh')
funcionario1.bonificar()
gerente1 = Gerente(123456, 25, 2500)
senha = int(input('Digite sua senha: '))
print(gerente1.autenticarSenha(senha))
print(gerente1.numero_funcionarios)
gerente1.bonificar()



