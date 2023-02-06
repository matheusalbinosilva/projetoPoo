#Crie a classe Emprestável com os atributos privados: título, nomePessoa, telefonePessoa e
#dataEmprestimo com seus getters e setters públicos.
#a. Crie a classe Livro e a classe CD, que herdem de Emprestável e tenham os atributos
#autor e artista, respectivamente, também privados com getters e setters públicos.
#b. Em uma lista, coloque pelo menos 3 itens emprestáveis diferentes de cada tipo,
#emprestados para pessoas diferentes.
#c. Percorra essa lista imprimindo o que foi emprestado para quem e quando, no
#seguinte formato: “O item X foi empresado para Y em Z”.
#d. Para utilizar o suporte a data, inclua no início do seu programa a linha “from


class Emprestavel:

    def __init__(self, titulo, nomePessoa, telefonePessoa, dataEmprestimo):
        self.titulo = titulo
        self.nomePessoa = nomePessoa
        self.telefonePessoa = telefonePessoa
        self.dataEmprestimo = dataEmprestimo

    @property
    def titulo(self):
        return self._titulo 
    
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def nomePessoa(self):
        return self._nomePessoa
    
    @titulo.setter
    def nomePessoa(self, valor):
        self._nomePessoa = valor

    @property
    def telefonePessoa(self):
        return self._telefonePessoa
    
    @titulo.setter
    def telefonePessoa(self, valor):
        self._telefonePessoa = valor    

    @property
    def dataEmprestimo(self):
        return self._dataEmprestimo
    
    @titulo.setter
    def dataEmprestimo(self, valor):
        self._dataEmprestimo = valor    


lista = []
pessoa1 = Emprestavel('Livro', 'Joao', 999418881,'02/01/2023')
pessoa2 = Emprestavel('Caderno', 'Nina', 999417781, '21/02/2023')
pessoa3 = Emprestavel('Vinil', 'nilsa', 999416681, '12/02/2023')
lista.append(pessoa1._titulo)
lista.append(pessoa1._nomePessoa)
lista.append(pessoa1._dataEmprestimo)
lista.append(pessoa2._titulo)
lista.append(pessoa2._nomePessoa)
lista.append(pessoa2._dataEmprestimo)
lista.append(pessoa3._titulo)
lista.append(pessoa3._nomePessoa)
lista.append(pessoa3._dataEmprestimo)
print(f'O item {lista[0]} foi empresado para {lista[1]}  em {lista[2]}')
print(f'O item {lista[3]} foi empresado para {lista[4]}  em {lista[5]}')
print(f'O item {lista[6]} foi empresado para {lista[7]}  em {lista[8]}')


