#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material 

    def mostraCor(self):
        print(self.cor)
    
    
    def trocaCor(self):
        self.cor = 'Verde'
        print(self.cor)

    


b1 = Bola('Azul', '70', 'couro')
b1.mostraCor()
b1.trocaCor()

