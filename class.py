class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura
    
    def envelhecer(self):
        self.idade += 1
        
    
    def engordar(self, kg):
        self.peso += kg
        

    def emagrecer(self, kg):
        self.peso -= kg
        return self.peso
    
    def crescer(self):
        if self.idade <= 21:
            self.altura += 0.5

pessoa1 = Pessoa('Matheus', 18, 80, 180)
pessoa2 = Pessoa('Romulo', 43, 43, 185)

while pessoa1.idade < 21:
    pessoa1.crescer()
    pessoa1.envelhecer()
print(f'{pessoa1.nome} tera {pessoa1.altura}cm ao atingir {pessoa1.idade}')
    