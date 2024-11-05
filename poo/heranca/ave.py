from animal import Animal

class Ave(Animal):

    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade, raca)

    def emitir_som(self):
        return 'Piu Piu'