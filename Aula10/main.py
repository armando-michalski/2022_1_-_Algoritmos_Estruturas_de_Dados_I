# 1)   Construir código necessário em Python para implementar o seguinte projeto: 
#      Uma classe abstrata chamada de Computador que contém os atributos/propriedades modelo, cor e preço. 
#      Esta classe também possui um método getInformacoes() que retorna todos os valores dos atributos. 
#      Esta classe também possui um método abstrato cadastrar(). ---ATENCAO

# 2)   O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Computador. 
#      A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte.
#      Esta classe reimplementa o método getInformacoes() herdado de computador.

# 3)   A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. 
#      Esta classe reimplementa o método getInformacoes() herdado de Computador.

# 4)   Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.

from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

# Não podemos instanciar um objeto de uma classe abstrata
# c = Computador()
# c.imprimir()
# c.imprimirEspecifico()



c1 = Desktop("Mac-DESKTOP", "Branco", "5000")

c1.cadastrar("PC-DESKTOP", "Branco", "5000")

c1.cadastrar("PC-DESKTOP", "Branco", "5000", "800")

c1.imprimirInformacoes()

print(c1.getInformacoesCompletas())


print("--------------------------------------")


c2 = Notebook("Mac-NOTEBOOK", "Branco", "5000")

c2.cadastrar("PC-NOTEBOOK", "Branco", "5000")

c2.cadastrar("PC-NOTEBOOK", "Branco", "5000", "50")

c2.imprimirInformacoes()

print(c2.getInformacoesCompletas())