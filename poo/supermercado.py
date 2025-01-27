class Produto:
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = preco
    
    def __str__(self):
        return f"{self._descricao} - {self._preco:.2f}"
    

class ProdutoEstoque(Produto):
    def __init__(self, descricao, preco):
        super().__init__(descricao, preco)
        self._estoque = 0.0
        
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco
        
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def preco(self, descricao):
        self._descricao = descricao
    
    def entrada(self, quantidade):
        self._estoque += quantidade
        
    def saida(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False
    
    def __str__(self):
        texto = super().__str__()
        texto += f'. Estoque: {self._estoque:.3f}'
        return texto
        
class ProdutoVenda(Produto):
    def __init__(self, descricao, preco, quantidade):
        super().__init__(descricao, preco)
        self._quantidade = quantidade
    
    @property  
    def total(self):
        return self._quantidade * self._preco
    
    def __str__(self):
        texto = super().__str__()
        texto += f". Qtde: {self._quantidade:.3f}."
        texto += f" Total: R$ {self.total:.2f}"
        return texto
    
class Venda:
    def __init__(self):
        self._produtos = []
        self._total = 0.0
        
    @property
    def total(self):
        return self._total
    
    @property
    def numero_produtos(self):
        return len(self._produtos)
    
    def adiciona_produto(self, produto):
        self._produtos.append(produto)
        self._total += produto.total
        
    def __str__(self):
        texto = '\n' + '-' * 50
        texto += '\nProdutos:'
        for produto in self._produtos:
            texto += '\n' + str(produto)
        texto += '\n' + '-' * 50
        texto += f'Total da venda: R$ {self._total:.2f}'
        texto += '\n' + '-' * 50
        return texto


class Caixa:
    def __init__(self):
        self._produtos = {}
        self._vendas = []
    
    @classmethod    
    def menu(cls):
        print()
        print("*" * 35)
        print("*              CAIXA              *")
        print("*" * 35)
        print("(C) Cadastrar/atualizar produto ")
        print("(E) Entrada de estoque ")
        print("(V) Vender ")
        print("(R) Relatório de vendas ")
        print("(S) Sair ")
        print("*" * 35)
        escolha = input("Informe sua opção: ").upper()
        return escolha
        
Caixa.menu()