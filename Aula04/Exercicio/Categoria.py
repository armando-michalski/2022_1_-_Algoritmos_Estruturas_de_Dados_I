class Categoria:

    def __init__(self, cod = "0", nomeCat = "Sem Nome"):
        self.codigo = cod
        self.nome = nomeCat

    def cadastrar(self):
        print("Codigo: ", self.codigo)
        print("Nome: ", self.nome)
        print("Categoria cadastrada com sucesso!")