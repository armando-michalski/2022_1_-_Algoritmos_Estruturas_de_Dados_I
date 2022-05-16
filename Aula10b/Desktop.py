from Computador import Computador

class Desktop(Computador): # Classe Desktop herda de Computador
    
    def __init__(self, modeloD, corD, precoD, potenciaDaFonteD = 500):
        super().__init__(modeloD, corD, precoD)
        self.potenciaDaFonte = potenciaDaFonteD # Sem underline é publico

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

    
    #METODO - CADASTRAR
    def cadastrar(self, modeloA, corA, precoA, potenciaDaFonteA = None):
        super().__modelo = modeloA
        super().__cor = corA
        super().__preco = precoA
        self.potenciaDaFonte = potenciaDaFonteA


    #METODO - GET INFORMACOES
    def getInformacoes(self):
        return [super().__modelo, super().__cor, super().__preco, self.potenciaDaFonte]