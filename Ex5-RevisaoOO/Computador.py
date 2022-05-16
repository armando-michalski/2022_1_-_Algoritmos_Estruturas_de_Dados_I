from abc import ABCMeta, abstractmethod # Auto-import

class Computador(metaclass=ABCMeta): # Sinalizando que essa classe será um classe abstrata

    def __init__(self, modeloC, corC, precoC):
        self.__modelo = modeloC
        self.__cor = corC
        self.__preco = precoC


    #MODELO
    @property # Declaração de atributos na forma de propriedades
    def modelo(self):
        pass

    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        pass


    #COR
    @property # Declaração de atributos na forma de propriedades
    def cor(self):
        pass

    @cor.setter
    @abstractmethod # Metodo abstrato só pode ser declarado dentro de uma classe abstrata
    def cor(self, valor):
        pass

    
    #PRECO
    @property # Declaração de atributos na forma de propriedades
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, valor):
        pass


    #METODO CONCRETO - IMPRIMIR
    def imprimir(self): # Pode ser chamado diretamente
        print("Modelo: ", self.__modelo)
        print("Cor: ", self.__cor)
        print("Preço: ", self.__preco)


    #METODO ABSTRATO - IMPRIMIR
    @abstractmethod # Necessario ser reimplementado
    def imprimirEspecifico(self):
        pass


    #METODO CONCRETO - GET INFORMAÇÕES
    def getInformacoes(self): # Esse metodo deve ser reimplementado pelas subclasses Desktop e Notebook
        return [self.__modelo, self.__cor, self.__preco]



    #METODO ABSTRATO - CADASTRAR
    @abstractmethod
    def cadastrar(self): # Esse metodo deve ser reimplementado pelas subclasses Desktop e Notebook
        pass


    #METODO CONCRETO - SET INFORMAÇÕES
    def setInformacoes(self, modeloT, corT, precoT):
        self.__modelo = modeloT
        self.__cor = corT
        self.__preco = precoT