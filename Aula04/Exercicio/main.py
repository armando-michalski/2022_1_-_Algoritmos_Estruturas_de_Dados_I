from Produto import Produto
from Categoria import Categoria

c1 = Categoria( 2 , "Bebidas")
p1 = Produto( 1 , "Coca-Cola 2L", 7.99 , 50 , c1)
p1.cadastrar()

p2 = Produto()

p2.setCategoria()

p2.cadastrar()