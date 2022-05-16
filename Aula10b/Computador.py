from abc import ABCMeta, abstractmethod # Auto-import

class Computador(metaclass=ABCMeta): # Sinalizando que essa classe será um classe abstrata

    def __init__(self, modeloC, corC, precoC):
        self.__modelo = modeloC
        self.__cor = corC
        self.__preco = precoC


    #ATRIBUTO - MODELO
    @property # Declaração de atributos na forma de propriedades
    def modelo(self):
        pass

    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        pass


    #ATRIBUTO - COR
    @property # Declaração de atributos na forma de propriedades
    def cor(self):
        pass

    @cor.setter
    @abstractmethod # Metodo abstrato só pode ser declarado dentro de uma classe abstrata
    def cor(self, valor):
        pass

    
    #ATRIBUTO - PRECO
    @property # Declaração de atributos na forma de propriedades
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, valor):
        pass


    #METODO - GET INFORMAÇÕES
    @abstractmethod
    def getInformacoes(self): # Esse metodo deve ser reimplementado pelas subclasses Desktop e Notebook
        pass


    #METODO - CADASTRAR
    @abstractmethod
    def cadastrar(self): # Esse metodo deve ser reimplementado pelas subclasses Desktop e Notebook
        pass
