from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, codigoAG = "000", nomeAG = "Sem Nome", matriculaAG = "000000000", semestreAG = "0"):
        super().__init__(codigoAG, nomeAG, matriculaAG)
        self.semestre = semestreAG

    def __str__(self):
        texto = "\nSemestre: " + self.semestre
        return super().__str__() + texto

    def imprimir(self):
        print("\nImpressão pelo método IMPRIMIR")
        print(super().__str__())
        print("Semestre:", self.semestre)