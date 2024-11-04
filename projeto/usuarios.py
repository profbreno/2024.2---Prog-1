class Usuarios:
    def __init__(self, nome, email, telefone, data_nascimento, endereco, data_cadastro):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.data_cadastro = data_cadastro

    def login(self):
        pass
    def __str__(self):
        return f'Usuario: {self.nome}'