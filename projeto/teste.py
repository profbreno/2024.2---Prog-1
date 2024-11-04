
from funcionarios import Funcionario
from clientes import Cliente

fulano = Funcionario('Fulano', 'fulano@gmail', '999999999', '1990-01-01', 'Rua 1', '2020-01-01', 1000, 'Fisioterapeuta')
print(fulano.login())

ciclano = Cliente('123', 'Ciclano', 'ciclano@gmail', '888888888', '1990-01-01', 'Rua 2', '2020-01-01')
print(ciclano.login())