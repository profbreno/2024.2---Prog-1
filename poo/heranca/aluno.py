class Aluno:
    def __init__(self, nome, idade, endereco_residencial, endereco_profisssional, matricula):
        self.nome = nome
        self.idade = idade
        self.endereco_residencial = endereco_residencial
        self.endereco_profisssional = endereco_profisssional
        self.matricula = matricula
        assinaturas = []

    def assinar(self, plano):
        self.assinaturas.append(plano)

