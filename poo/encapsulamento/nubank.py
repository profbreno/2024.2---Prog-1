class conta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo')
        else:
            self.__saldo = saldo

class contaCorrente(conta):
    def __init__(self, numero, saldo, limite):
        super().__init__(numero, saldo)
        self.__limite = limite
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

nubank = contaCorrente(123, 1000, 500)
print(nubank.saldo)
nubank.saldo = 500
print(nubank.saldo)