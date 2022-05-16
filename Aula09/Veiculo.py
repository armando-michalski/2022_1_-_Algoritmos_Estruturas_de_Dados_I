from abc import ABCMeta, abstractmethod


class Veiculo( metaclass=ABCMeta ):

	def __init__(self, modelo, ano = None):
		self.__modelo = modelo #__ significa fortemente privado, ou seja não pode utilizar o atributo modelo, sem passar pela property
		self.__ano = ano

	#METODO ACESSOR (GETTER)
	@property
	def modelo(self):
		pass

	#MÉTODO MODIFICADOR (SETTER)
	@modelo.setter
	@abstractmethod #Obrigatoriamente deve ser reimplementado
	def modelo( self, valor):
		pass

	#METODO ACESSOR (GETTER)
	@property
	def ano(self):
		pass
	
	#MÉTODO MODIFICADOR (SETTER)
	@ano.setter
	@abstractmethod
	def ano( self, valor):
		pass

	#MÉTODO NÃO-ABSTRATO = PODE SER RE-ESCRITO
	def imprimir(self):
		print("Modelo: ", self.__modelo)
		print("Ano: ", self.__ano)

	#MÉTODO ABSTRATO = DEVE SER RE-ESCRITO
	@abstractmethod
	def imprimirEspecifico(self):
		pass