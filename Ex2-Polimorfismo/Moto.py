from Automovel import Automovel

class Moto(Automovel):

    def __init__(self, marcaM, qtdRodasM, modeloM, velocidadeM, potenciaDoMotorM, partidaEletricaM):
        super().__init__(marcaM, qtdRodasM, modeloM, velocidadeM, potenciaDoMotorM)
        self.partidaEletrica = partidaEletricaM

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Partida eletrica: ", self.partidaEletrica)