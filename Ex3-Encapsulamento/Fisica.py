from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, codigoF, nomeF, enderecoF, telefoneF, cpfF, idadeF, pesoF, alturaF):
        super().__init__(codigoF, nomeF, enderecoF, telefoneF)
        self.__cpf = cpfF
        self.idade = idadeF
        self.peso = pesoF
        self.altura = alturaF

    def imprimeCPF(self):
        print("CPF: ", self.__cpf)

    def __calculaIMC(self):
        imc = self.peso / (self.altura * self.altura)
        print("IMC: ", imc)