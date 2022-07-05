from Ferramenta import Ferramenta

class Furadeira(Ferramenta):

    def __init__(self, nomeF, tensaoF, precoF, potenciaF):
        super().__init__(nomeF, tensaoF, precoF)
        self._potencia = potenciaF # Fracamente privado
    

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
        return [x[0], x[1], x[2], self._potencia]

    #METODO CONCRETO - CADASTRAR
    def cadastrar(self, nomeA, tensaoA, precoA, potenciaA):
        super().setInformacoes(nomeA, tensaoA, precoA)
        self._potencia = potenciaA

    #METODO CONCRETO (auxiliar) - IMPRIMIR VIA GET INFORMACOES (superclasse)
    def imprimirInformacoes(self):
        x = super().getInformacoesTeste()
        print("Nome: ", x[0])
        print("Tensao: ", x[1])
        print("Preco: ", x[2])
        print("Potencia: ", self._potencia)