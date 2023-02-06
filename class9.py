class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'O restaurante {self.name} é do tipo {self.cuisine_type}')

    def open_restaurant(self):
        print(f'O restaurante {self.name} está aberto')


restaurant01 = Restaurant('Messito`s', 'Japones')
restaurant02 = Restaurant('Zogos', 'Chilena')
restaurant03 = Restaurant('Finus', 'Brasileiro')

restaurant01.describe_restaurant()
restaurant01.open_restaurant()
restaurant02.describe_restaurant()
restaurant02.open_restaurant()
restaurant03.describe_restaurant()
restaurant03.open_restaurant()

