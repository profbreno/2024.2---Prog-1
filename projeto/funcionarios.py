from usuarios import Usuarios

class Funcionario(Usuarios):
    def __init__(self, nome, email, telefone, data_nascimento, endereco, data_cadastro, salario, especialidade):
        super().__init__(nome, email, telefone, data_nascimento, endereco, data_cadastro)
        self.salario = salario
        self.especialidade = especialidade
    
    def login(self):
        return "Funcionario logado com sucesso!"

    def __str__(self):
        return f'Funcionario: {self.nome}'