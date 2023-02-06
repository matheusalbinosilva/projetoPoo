#Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:

    def __init__(self, nome, bucho='vazio'):
        self.nome = nome
        self.bucho = bucho
    
    def comer(self):
        if self.bucho == 'cheio':
            print('Nao pode comer agora, pois esta cheio')
        self.bucho = 'cheio'

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho = 'vazio'

    
    
macaco1 = Macaco('Chimpan')
macaco2 = Macaco('Creps')
macaco1.comer()
print(macaco1.bucho)
macaco1.comer()
macaco2.verBucho()
print(macaco2.nome)

