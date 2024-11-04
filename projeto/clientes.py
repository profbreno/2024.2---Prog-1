'''
Aqui teremos a classe principal de clientes para uma aplicação de studio de fisioterapia e pilates.
nome: str
email: str
telefone: str
data_nascimento: date
endereco: str
data_cadastro: date

# Relacionamentos
agendamentos
avaliacoes 
prontuarios
financeiro
mensalidades
'''

class Cliente:
    def __init__(self, nome, email, telefone, data_nascimento, endereco, data_cadastro):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.data_cadastro = data_cadastro
        
    def __str__(self):
        return f'Cliente: {self.nome}'