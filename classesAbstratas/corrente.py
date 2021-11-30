from conta import Conta

class ContaCorrent(Conta):
    def __init__(self, agencia, numero, saldo, limite = 100):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()