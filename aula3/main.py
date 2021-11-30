from produto import Produto

p1 = Produto('mesa', 'R$ 500.0')

p1.desconto(70)
print(f'Valor do produto: R$ {p1.preco}')