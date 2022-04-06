from Categoria import Categoria

class Produto:

    def __init__(self, cod = None, nomeP = None, precoP = None, qtd = None, catP = None):
        self.codigo = cod
        self.nome = nomeP
        self.preco = precoP
        self.quantidade = qtd
        self.cat = catP

    def cadastrar(self):
        print("Codigo: ", self.codigo)
        print("Nome: ", self.nome)
        print("Preço: ", self.preco)
        print("Quantidade: ", self.quantidade)
        print("Categoria: ", self.cat.codigo, " - ", self.cat.nome)
        #print("Categoria: ", self.cat")
        print("Cadastrado com sucesso!")

    def setCategoria(self, categ = Categoria()):
        self.cat = categ

    def __str__(self):
        return str(self.codigo) + " - " + self.nome