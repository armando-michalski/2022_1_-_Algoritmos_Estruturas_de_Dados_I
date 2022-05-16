from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigoAEM = "000", nomeAEM = "Sem Nome", matriculaAEM = "000000000", anoAEM = "0"):
        super().__init__(codigoAEM, nomeAEM, matriculaAEM)
        self.ano = anoAEM

    def __str__(self):
        return super().__str__() + "\nAno: " + self.ano

    def imprimir(self):
        print("\nImpressão pelo método IMPRIMIR")
        print(super().__str__())
        print("Ano:", self.ano)
