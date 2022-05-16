from Computador import Computador

class Notebook(Computador):
    
    def __init__(self, modeloN, corN, precoN, tempoDeBateriaN = "10"):
        super().__init__(modeloN, corN, precoN)
        self.__tempoDeBateria = tempoDeBateriaN
    
    #MODELO - GETTER (MÉTODO ACESSOR)
    @property
    def modelo(self): # Metodo acessor
        return self.__modelo

    #MODELO - SETTER (MÉTODO MODIFICADOR)
    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor


    #COR - GETTER (MÉTODO ACESSOR)
    @property
    def cor(self):
        return self.__cor

    #COR - SETTER (MÉTODO MODIFICADOR)
    @cor.setter #SETTER
    def cor(self, valor):
        self.__cor = valor


    #PRECO - GETTER (MÉTODO ACESSOR)
    @property
    def preco(self):
        return self.__preco

    #PRECO - SETTER (MÉTODO MODIFICADOR)
    @preco.setter
    def preco(self, valor):
        self.__preco = valor


    #METODO (EXEMPLO) - IMPRIMIR VIA IMPRIMIR
    def imprimirEspecifico(self): # Polimorfismo de sobreescrita
        super().imprimir()
        print("Tempo: ", str(self.__tempoDeBateria))


    #METODO (TESTE) - IMPRIMIR VIA GET INFORMACOES
    def imprimirInformacoes(self):
        x = super().getInformacoes()
        print("Modelo: ", x[0])
        print("Cor: ", x[1])
        print("Preco: ", x[2])
        print("Tempo: ", self.__tempoDeBateria)


    #METODO (SOLICITADO) - CADASTRAR
    def cadastrar(self, modeloB, corB, precoB, tempoDeBateriaB = None):
        super().setInformacoes(modeloB, corB, precoB)
        self.__tempoDeBateria = tempoDeBateriaB


    #METODO (SOLICITADO) - GET INFORMACOES
    def getInformacoesCompletas(self):
        x = super().getInformacoes()
        return [x[0], x[1], x[2], self.__tempoDeBateria]