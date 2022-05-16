from Automovel import Automovel

class Carro(Automovel):

    def __init__(self, marcaC, qtdRodasC, modeloC, velocidadeC, potenciaDoMotorC, qtdPortasC):
        super().__init__(marcaC, qtdRodasC, modeloC, velocidadeC, potenciaDoMotorC)
        self.qtdPortas = qtdPortasC

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Quantidade de portas: ", self.qtdPortas)