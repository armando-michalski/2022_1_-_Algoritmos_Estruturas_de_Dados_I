from abc import ABCMeta, abstractmethod

class Ferramenta(metaclass=ABCMeta):

    def __init__(self, nomeFF, tensaoFF, precoFF):
        self.__nome = nomeFF
        self.__tensao = tensaoFF
        self.__preco = precoFF
    

    #NOME - METODO ACESSOR (GETTER)
    @property # Declaração de atributos na forma de propriedades
    def nome(self):
        pass

    #NOME - METODO MODIFICADOR (SETTER)
    @nome.setter
    @abstractmethod
    def nome(self, valor):
        pass


    #TENSAO - METODO ACESSOR (GETTER)
    @property # Declaração de atributos na forma de propriedades
    def tensao(self):
        pass

    #TENSAO - METODO MODIFICADOR (SETTER)
    @tensao.setter
    @abstractmethod # Metodo abstrato só pode ser declarado dentro de uma classe abstrata
    def tensao(self, valor):
        pass


    #PRECO - METODO ACESSOR (GETTER)
    @property # Declaração de atributos na forma de propriedades
    def preco(self):
        pass

    #PRECO - METODO MODIFICADOR (SETTER)
    @preco.setter
    @abstractmethod
    def preco(self, valor):
        pass


    #METODO CONCRETO - GET INFORMAÇÕES
    def getInformacoes(self): # Esse metodo deve ser reimplementado pelas subclasses Desktop e Notebook
        pass

    #METODO ABSTRATO - CADASTRAR
    @abstractmethod
    def cadastrar(self): # Esse metodo deve ser reimplementado pelas subclasses Desktop e Notebook
        pass

    #METODO CONCRETO (auxiliar) - SET INFORMAÇÕES
    def setInformacoes(self, nomeT, tensaoT, precoT):
        self.__nome = nomeT
        self.__tensao = tensaoT
        self.__preco = precoT
    
    #METODO CONCRETO (auxiliar) - GET INFORMAÇÕES
    def getInformacoesTeste(self): # Esse metodo deve ser reimplementado pelas subclasses Desktop e Notebook
        return [self.__nome, self.__tensao, self.__preco]