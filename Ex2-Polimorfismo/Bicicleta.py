from Veiculo import Veiculo

class Bicicleta(Veiculo):
    
    def __init__(self, marcaB, qtdRodasB, modeloB, velocidadeB, numMarchasB, bagageiroB):
        super().__init__(marcaB, qtdRodasB, modeloB, velocidadeB)
        self.numMarchas = numMarchasB
        self.bagageiro = bagageiroB

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Numero de marchas: ", self.numMarchas)
        print("Bagageiro: ", self.bagageiro)
