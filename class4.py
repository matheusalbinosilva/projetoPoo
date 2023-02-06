#Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.


class Tv:

    def __init__(self, canal):
        self.canal = canal
        while True:
            if self.canal < 0 or self.canal > 50:
                self.canal = int(input('Digite o canal de sua escolha! 0 / 50:  '))
            else:
                print(self.canal)
                break
           
    def volume(self):
        if volume in 'aumentar':
            print(f'Aumentando o volume...')
        if volume in 'diminuir':
            print(f'Diminuindo volume...')

        
canal = int(input('Digite o canal de sua escolha 0 / 50:  '))
canal1 = Tv(canal)
canal1.canal
volume = str(input('Você quer aumentar ou dimnuir o volume: ')).strip().lower()[0]
canal1.volume()