from abc import ABCMeta, abstractmethod

class ContaBancaria(metaclass=ABCMeta):

    #METODO CADASTRAR
    @abstractmethod
    def cadastrar(self):
        pass

    #METODO DEPOSITAR
    @abstractmethod
    def depositar(self):
        pass