from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

a1 = Aluno("001", "João", "111222333")
a1.imprimir()
print("\n-----------\n")
print(a1)

ag1 = AlunoGraduacao("002", "Lucas", "444555666", "2")
print("\n-----------\n")
print(ag1)
ag1.imprimir()

aem1 = AlunoEnsinoMedio("003", "Pedro", "777888999", "3")
print("\n-----------\n")
print(aem1)
aem1.imprimir()