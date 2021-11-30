class Produto:
    def __init__(self, nome, preco, vendido = False):
        self._nome = nome
        self._preco = preco
        self.vendido = vendido
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    def comprar(self):
        if not self.vendido:
            print('Vendido')
        else:
            print(f'Produto {self.nome} indisponível')
        
        self.vendido = True
    
    def desfazer_compra(self):
        if self.vendido:
            print('Compra cancelada!')
        self.vendido = False

produto1 = Produto('Mesa', 500.0)
print(produto1.nome)
produto1.comprar()
produto1.desfazer_compra()
produto1.comprar()
produto1.comprar()
produto1.desfazer_compra()
produto1.comprar()
produto1.comprar()
produto1.desfazer_compra()
produto1.comprar()
produto1.comprar()