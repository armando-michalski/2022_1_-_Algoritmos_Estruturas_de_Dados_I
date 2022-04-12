class Pessoa:

    def __init__(self, nome = "Sem Nome", telefone = "1234"):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return "Nome: " + self.nome + "\nTelefone: " + self.telefone
