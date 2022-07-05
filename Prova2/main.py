"""
Construa um software em Python que implemente uma Pilha de livros e uma Pilha de Revistas.
As classes Livro e Revista herdam da classe Publicação, os atributos e métodos comuns às duas classes.
A classe Livro é composta dos atributos id, data de publicação, título e autor. O atributo autor é fracamente privado.
A classe Revista é composta dos atributos id, data de publicação, preço. O atributo preço é fortemente privado.
Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.
Implemente uma tela com um menu (funcionando) que permita ao usuário:
-> Adicionar e remover livros da Pilha.
-> Adicionar e remover revistas da Pilha.
-> Imprimir a Pilha de livros e a Pilha de revistas.
"""

from Publicacao import Publicacao
from Livro import Livro
from Revista import Revista
from Pilha import Pilha

l1 = Livro("L1A", "1A/1A/1A", "Artigo1A", "Autor1A")
l1.cadastrar("L1B", "1B/1B/1B", "Artigo1B", "Autor1B")
l1.imprimirInformacoes()

l2 = Livro("L2A", "2A/2A/2A", "Artigo2A", "Autor2A")
l2.cadastrar("L2B", "2B/2B/2B", "Artigo2B", "Autor2B")
l2.imprimirInformacoes()

l3 = Livro("L3A", "3A/3A/3A", "Artigo3A", "Autor3A")
l3.cadastrar("L3B", "3B/3B/3B", "Artigo3B", "Autor3B")
l3.imprimirInformacoes()

print("\n-----------\n")

r1 = Revista("R1A", "1A/1A/1A", "111AAA")
r1.cadastrar("R1B", "1B/1B/1B", "111BBB")
r1.imprimirInformacoes()

r2 = Revista("R2A", "2A/2A/2A", "222AAA")
r2.cadastrar("R2B", "2B/2B/2B", "222BBB")
r2.imprimirInformacoes()

r3 = Revista("R3A", "3A/3A/3A", "333AAA")
r3.cadastrar("R3B", "3B/3B/3B", "333BBB")
r3.imprimirInformacoes()

print("\n-----------\n")

livros = Pilha()
livros.imprimir()
livros.adicionar(l1)
livros.adicionar(l2)
livros.adicionar(l3)
livros.remover()

print("\n-----------\n")

revistas = Pilha()
revistas.imprimir()
revistas.adicionar(r1)
revistas.adicionar(r2)
revistas.adicionar(r3)
revistas.remover()


# MENU DE FUNCIONALIDADES
while True:
    print(
        """
         MENU:
         0- Finalizar o programa
         1- Adicionar livros na Pilha1.
         2- Adicionar revista na Pilha2.
         3- Remover livros da Pilha1.
         4- Remover revistas da Pilha2.
         5- Imprimir a Pilha1 de livros.
         6- Imprimir a Pilha2 de revistas.
         """)

    teclado = input('Digite um numero do MENU acima: ')

    #livros = Pilha()
    #revistas = Pilha()

    if teclado == '0':
        break

    elif teclado == '1':
        idA = input("Informe Id: ")
        dataA = input("Informe Data: ")
        tituloA = input("Informe Titulo: ")
        autorA = input("Informe Autor: ")
        lA = Livro(idA, dataA, tituloA, autorA)
        livros.adicionar(lA)

    elif teclado == '2':
        idB = input("Informe Id: ")
        dataB = input("Informe Data: ")
        precoB = input("Informe Preco: ")
        rB = Livro(idB, dataB, precoB)
        livros.adicionar(rB)

    elif teclado == '3':
        livros.remover()

    elif teclado == '4':
        revistas.remover()

    elif teclado == '5':
        livros.imprimir()

    elif teclado == '6':
        revistas.imprimir()

print('Programa finalizado!')
