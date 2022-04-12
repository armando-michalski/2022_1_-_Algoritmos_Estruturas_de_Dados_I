from mailbox import NoSuchMailboxError


class Aluno:
    def __init__(self, codigoA = "000", nomeA = "Sem Nome", matriculaA = "000000000"):
        self.codigo = codigoA
        self.nome = nomeA
        self.matricula = matriculaA

    def __str__(self):
        return "Código: " + self.codigo + "\nNome: " + self.nome + "\nMatrícula: " + self.matricula

    def imprimir(self):
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Matrícula: ", self.matricula)