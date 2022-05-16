from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica


p1 = Pessoa(1, "Carlos", "Rua Nilo 400", 3344556677)
p1.imprimeNome()
p1.imprimeTelefone()

print("----------")

p2 = Fisica(2, "Joana", "Rua Nilo 700", 5566778899, 888999888999, 30, 80, 1.88)
p2.imprimeNome()
p2.imprimeTelefone()
p2.imprimeCPF()
#p2.calculaIMC() #É possivel se o metodo não for privado
#p2.__calculaIMC() #Mas sendo um metodo privado, não é possivel aceesar

print("----------")

p3 = Juridica(3, "Renner", "Rua Nilo 900", 2233445566, "88899988-000189", 6230, 10)
p3.imprimeNome()
p3.imprimeTelefone()
p3.imprimeCNPJ()
#p3.emitirNotaFiscal() #É possivel se o metodo não for privado
#p3._emitirNotaFiscal() #Mas sendo um metodo privado, não é possivel aceesar
