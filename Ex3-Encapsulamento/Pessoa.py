class Pessoa:



    def __init__(self, codigoP, nomeP, enderecoP, telefoneP):
        self.__codigo = codigoP
        self.nome = nomeP
        self._endereco = enderecoP
        self.__telefone = telefoneP

    def imprimeNome(self):
        print("Nome: ", self.nome)

    def imprimeTelefone(self):
        print("Telefone: ", self.__telefone)
