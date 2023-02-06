#Crie uma classe que modele uma conta corrente
#a) Atributos: numero da conta, nome do correntista e saldo ´
#(b) Metodos: alterar nome, dep ´ osito e saque; No construtor, saldo ´ e opcional, com valor ´
#default zero e os demais atributos sao obrigat ˜ orios. ´


class Conta_corrente:

    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        self.nome_correntista = 'fufu'
        print(self.nome_correntista)

    def deposito_saque(self):



conta = Conta_corrente(4312, 'matheus', 2000)
print(conta.nome_correntista)
conta.alterar_nome()