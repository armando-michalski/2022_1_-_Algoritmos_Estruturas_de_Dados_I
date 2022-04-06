from Pessoa import Pessoa

class Fisica(Pessoa): #A classe Física (FILHA) herda da classe Pessoa (PAI)

    def __init__(self, idade):
        super().__init__()
        self.idade = idade
        print("Pessoa física construída")

    def __str__(self): 
        #A classe FILHA esta aproveitando o que o PAI faz, mais alguma coisa
        return super().__str__() + "\nIdade: " + str(self.idade)