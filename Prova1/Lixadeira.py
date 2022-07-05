from Ferramenta import Ferramenta

class Lixadeira(Ferramenta):

    def __init__(self, nomeL, tensaoL, precoL, rotacoesL):
        super().__init__(nomeL, tensaoL, precoL)
        self.__rotacoes = rotacoesL # Fortemente privado
    

    #NOME - METODO ACESSOR (GETTER)
    @property
    def nome(self):
        return self.__nome

    #NOME - METODO MODIFICADOR (SETTER)
    @nome.setter
    def nome(self, valor):
        self.__nome = valor


    #TENSAO - METODO ACESSOR (GETTER)
    @property
    def tensao(self):
        return self.__tensao

    #TENSAO - METODO MODIFICADOR (SETTER)
    @tensao.setter
    def tensao(self, valor):
        self.__tensao = valor


    #PRECO - METODO ACESSOR (GETTER)
    @property
    def preco(self):
        return self.__preco

    #PRECO - METODO MODIFICADOR (SETTER)
    @preco.setter #SETTER
    def preco(self, valor):
        self.__preco = valor


    #METODO CONCRETO - GET INFORMACOES
    def getInformacoes(self):
        x = super().getInformacoesTeste()
        return [x[0], x[1], x[2], self.__rotacoes]

    #METODO CONCRETO - CADASTRAR
    def cadastrar(self, nomeB, tensaoB, precoB, rotacoesB):
        super().setInformacoes(nomeB, tensaoB, precoB)
        self.__rotacoes = rotacoesB

    #METODO CONCRETO (auxiliar) - IMPRIMIR VIA GET INFORMACOES (superclasse)
    def imprimirInformacoes(self):
        x = super().getInformacoesTeste()
        print("Nome: ", x[0])
        print("Tensao: ", x[1])
        print("Preco: ", x[2])
        print("Rotacoes: ", self.__rotacoes)