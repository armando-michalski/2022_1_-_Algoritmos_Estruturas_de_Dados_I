class Veiculo():
    
    def __init__(self, marcaV, qtdRodasV, modeloV, velocidadeV):
        self.marca = marcaV
        self.qtdRodas = qtdRodasV
        self.modelo = modeloV
        self.velocidadeAtual = velocidadeV
    
    def imprimirInformacoes(self):
        print("Marca: ", self.marca)
        print("Quantidade de rodas: ", self.qtdRodas)
        print("Modelo: ", self.modelo)
        print("Velocidade: ", self.velocidadeAtual)

    def imprimirVelocidade(self):
        print("Velocidade: ", self.velocidadeAtual)
    
    def acelerar(self, valorA):
        self.velocidadeAtual += valorA

    def frear(self, valorF):
        self.velocidadeAtual -= valorF
    