from Computador import Computador

class Notebook(Computador):
    
    def __init__(self, modeloN, corN, precoN, tempoDeBateriaN = "10"):
        super().__init__(modeloN, corN, precoN)
        self.__tempoDeBateria = tempoDeBateriaN
    
    #ATRIBUTO - MODELO
    @property #GETTER
    def modelo(self): # Metodo acessor
        return self.__modelo

    @modelo.setter #SETTER
    def modelo(self, valor):
        self.__modelo = valor


    #ATRIBUTO - COR
    @property #GETTER
    def cor(self): # Metodo acessor
        return self.__cor

    @cor.setter #SETTER
    def cor(self, valor):
        self.__cor = valor


    #ATRIBUTO - PRECO
    @property #GETTER
    def preco(self): # Metodo acessor
        return self.__preco

    @preco.setter #SETTER
    def preco(self, valor):
        self.__preco = valor

    
