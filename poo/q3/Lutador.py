class Lutador:

    def __init__(self, nome, energia, forca):
        self.nome = nome
        self.energia = energia
        self.forca = forca

    # Reduz a energia do lutador até um mínimo de 0
    def reduzirEnergia(self, energia):
        self.energia -= energia
    
    def aplicarGolpe(self, lutador):
        lutador.reduzirEnergia(self.forca)

    # Criar especial depois de aplicar 3 golpes