#O sistema possuirá uma classe abstrata chamada de Ferramenta que deve conter os atributos/propriedades nome, tensão e preço. 
#Esta classe também deve possuir um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

#O projeto também deve possuir as classes concretas, Furadeira e Lixadeira que herdam da classe Ferramenta.
#A classe Furadeira deve possuir o atributo/propriedade fracamente privado, potência. Esta classe reimplementa o método getInformacoes() herdado de Furadeira.
#A classe Lixadeira possui o atributo/propriedade fortemente privado, rotações. Esta classe reimplementa o método getInformacoes() herdado de Furadeira.


from Ferramenta import Ferramenta
from Furadeira import Furadeira
from Lixadeira import Lixadeira

f1 = Furadeira("F1", "110V", "R$1000", "700W")
f1.cadastrar("FF1", "110V", "R$1000", "700W")
f1.imprimirInformacoes()
print("Via GET INFORMACOES: ", f1.getInformacoes())

print("--------------------")

f2 = Lixadeira("F2", "220V", "R$500", "500W")
f2.cadastrar("FF2", "110V", "R$1000", "700W")
f2.imprimirInformacoes()
print("Via GET INFORMACOES: ", f2.getInformacoes())

print("--------------------")