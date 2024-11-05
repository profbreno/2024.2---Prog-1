from animal import Animal

class Cachorro(Animal):

    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca)

    def emitir_som(self):
        return 'Au Au'