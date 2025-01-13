from aluno import Aluno
from endereco import Endereco

endereco_residencial = Endereco('Rua 1', 123, 'Bairro 1', 'Cidade 1', 'Estado 1')
endereco_profissional = Endereco('Rua 2', 456, 'Bairro 2', 'Cidade 2', 'Estado 2')

breno = Aluno('Breno', 20, endereco_residencial, endereco_profissional, 123)

breno.assinar('Plano 1')
breno.assinar('Plano 2')