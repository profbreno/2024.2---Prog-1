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

from projeto.usuarios import Usuarios

class Cliente(Usuarios):
    def __init__(self, prontuario, nome, email, telefone, data_nascimento, endereco, data_cadastro):
        super().__init__(nome, email, telefone, data_nascimento, endereco, data_cadastro)
        self.prontuario = prontuario
        
    def __str__(self):
        return f'Cliente: {self.nome}'