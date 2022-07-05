from Publicacao import Publicacao

class Revista(Publicacao):

    def __init__(self, idR, dataR, precoR):
        super().__init__(idR, dataR)
        self.__preco = precoR

    def cadastrar(self, idR, dataR, precoR):
        super().setInformacoes(idR, dataR)
        self.__preco = precoR

    def imprimirInformacoes(self):
        x = super().getInformacoes()
        print("Id: ", x[0])
        print("Data: ", x[1])
        print("Preco: ", self.__preco)