from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, codigoJ, nomeJ, enderecoJ, telefoneJ, cnpjJ, inscricaoEstadualJ, quantidadeFuncionariosJ):
        super().__init__(codigoJ, nomeJ, enderecoJ, telefoneJ)
        self.__cnpjJ = cnpjJ
        self.__inscricaoEstadual = inscricaoEstadualJ
        self.quantidadeFuncionarios = quantidadeFuncionariosJ

    def imprimeCNPJ(self):
        print("CNPJ: ", self.__cnpjJ)

    def __emitirNotaFiscal(self):
        print("Teste NF") 