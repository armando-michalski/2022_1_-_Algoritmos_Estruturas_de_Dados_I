from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self, marcaA, qtdRodasA, modeloA, velocidadeA, potenciaDoMotorA):
        super().__init__(marcaA, qtdRodasA, modeloA, velocidadeA)
        self.potenciaDoMotor = potenciaDoMotorA

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Potencia do motor: ", self.potenciaDoMotor)