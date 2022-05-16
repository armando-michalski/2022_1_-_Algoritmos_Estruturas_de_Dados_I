from Computador import Computador

class Desktop(Computador): # Classe Desktop herda de Computador
    
    def __init__(self, modeloD, corD, precoD, potenciaDaFonteD = 500):
        super().__init__(modeloD, corD, precoD)
        self.potenciaDaFonte = potenciaDaFonteD # Sem underline é publico

    #MODELO - GETTER (MÉTODO ACESSOR)
    @property #GETTER
    def modelo(self): # Metodo acessor
        return self.__modelo

    #MODELO - SETTER (MÉTODO MODIFICADOR)
    @modelo.setter #SETTER
    def modelo(self, valor):
        self.__modelo = valor


    #COR - GETTER (MÉTODO ACESSOR)
    @property #GETTER
    def cor(self): # Metodo acessor
        return self.__cor

    #COR - SETTER (MÉTODO MODIFICADOR)
    @cor.setter #SETTER
    def cor(self, valor):
        self.__cor = valor


    #PRECO - GETTER (MÉTODO ACESSOR)
    @property #GETTER
    def preco(self): # Metodo acessor
        return self.__preco

    #PRECO - SETTER (MÉTODO MODIFICADOR)
    @preco.setter #SETTER
    def preco(self, valor):
        self.__preco = valor

    
    #METODO (EXEMPLO) - IMPRIMIR VIA METODO IMPRIMIR
    def imprimirEspecifico(self): # Polimorfismo de sobreescrita
        super().imprimir()
        print("Potencia: ", str(self.potenciaDaFonte))


    #METODO (TESTE) - IMPRIMIR VIA GET INFORMACOES
    def imprimirInformacoes(self):
        x = super().getInformacoes()
        print("Modelo: ", x[0])
        print("Cor: ", x[1])
        print("Preco: ", x[2])
        print("Potência: ", self.potenciaDaFonte)
    

    #METODO (SOLICITADO) - CADASTRAR
    def cadastrar(self, modeloA, corA, precoA, potenciaDaFonteA = None):
        super().setInformacoes(modeloA, corA, precoA)
        self.potenciaDaFonte = potenciaDaFonteA


    #METODO (SOLICITADO) - GET INFORMACOES
    def getInformacoesCompletas(self):
        x = super().getInformacoes()
        return [x[0], x[1], x[2], self.potenciaDaFonte]