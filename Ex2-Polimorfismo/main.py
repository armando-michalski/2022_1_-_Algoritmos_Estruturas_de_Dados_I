from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Carro import Carro
from Moto import Moto


v1 = Veiculo("Fiat", 4, "Uno", 100)
v1.imprimirInformacoes()

v1.acelerar(50)
v1.imprimirVelocidade()
v1.frear(40)
v1.imprimirVelocidade()

print("------------------------------")

v2 = Bicicleta("Trek", 2, "TK5000", 10, 18, True)
v2.imprimirInformacoes()

print("------------------------------")

v3 = Automovel("Ford", 4, "Ka", 200, "90CV")
v3.imprimirInformacoes()

print("------------------------------")

v4 = Carro("Citroen", 4, "C4", 300, "100CV", 4)
v4.imprimirInformacoes()

print("------------------------------")

v5 = Moto("Yamaha", 2, "Y700", 80, "50CV", True)
v5.imprimirInformacoes()