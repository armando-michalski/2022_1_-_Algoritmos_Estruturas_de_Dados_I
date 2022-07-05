from Publicacao import Publicacao

class Livro(Publicacao):

    def __init__(self, idL, dataL, tituloL, autorL):
        super().__init__(idL, dataL)
        self._titulo = tituloL
        self._autor = autorL

    def cadastrar(self, idL, dataL, tituloL, autorL):
        super().setInformacoes(idL, dataL)
        self._titulo = tituloL
        self._autor = autorL

    def imprimirInformacoes(self):
        x = super().getInformacoes()
        print("Id: ", x[0])
        print("Data: ", x[1])
        print("Titulo: ", self._titulo)
        print("Autor: ", self._autor)

    def __str__(self):
        texto =  "\nTitulo: " + self._titulo + "\nAutor: " + self._autor	
        return super().__str__() + texto