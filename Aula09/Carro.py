from Veiculo import Veiculo

class Carro( Veiculo ):

	def __init__(self, modelo, ano = None, portas = 2):
		super().__init__(modelo, ano)
		self.portas = portas

	#METODO ACESSOR (GETTER)
	@property
	def modelo(self):
		return self.__modelo

	#MÉTODO MODIFICADOR (SETTER)
	@modelo.setter 
	def modelo(self, valor):
		self.__modelo = valor

	#METODO ACESSOR (GETTER)
	@property
	def ano(self):
		return self.__ano

	#MÉTODO MODIFICADOR (SETTER)
	@ano.setter 
	def ano(self, valor):
		self.__ano = valor

	def imprimirEspecifico(self):
		super().imprimir()
		print("Portas: " , str(self.portas))

	
	

	