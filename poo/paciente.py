class Paciente:
    def __init__(self, nome, idade, genero):
        self._nome = nome
        self._idade = idade
        self._genero = genero
        self._anamneses = []
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
        
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero

    def adicionar_anamnese(self, anamnese):
        self._anamneses.append(anamnese)

    def remover_anamnese(self, anamnese):
        self._anamneses.remove(anamnese)

    def listar_anamneses(self):
        return [f"{anamnese._data} - {anamnese._descricao}" for anamnese in self._anamneses]


class Anamnese:
    def __init__(self, data, descricao):
        self._data = data
        self._descricao = descricao