#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro
#quantidadeCombustivel
#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class bombaCombustível:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        print(f'Contem {self.quantidadeCombustivel} litros de combustivel na bomba"')

    def abastecerPorValor(self, valor):
        self.valor = valor
        self.valor = self.valor / self.valorLitro
        print(f'Foi colocado {self.valor} litros de gasolina!')
        self.quantidadeCombustivel = self.quantidadeCombustivel - self.valor
        print(f'Atualizando a bomba {self.quantidadeCombustivel} litros')

    def abastecerPorLitro(self, litro):
        self.litro = litro
        self.litro = self.litro * self.valorLitro
        print(f'O valor a ser pago é R${self.litro} ')

    def alterarValor(self, novo_valor):
        self.novo_valor = novo_valor
        print(f'O novo valor do combustivel será R${self.novo_valor}')
    
    def alterarCombustivel(self, novo_combustivel):
        self.novo_combustivel = novo_combustivel
        print(self.novo_combustivel)

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.nova_quantidade = nova_quantidade
        print(self.nova_quantidade)





v1 = bombaCombustível('Gasolina', 5.00, 100)
valor = int(input('informe o valor que voce quer colocar de combustivel: '))
v1.abastecerPorValor(valor)
litro = int(input('informe a litragem que voce quer colocar de combustivel: '))
v1.abastecerPorLitro(litro)
v1.alterarValor(5.50)
v1.alterarCombustivel('Alcool')
