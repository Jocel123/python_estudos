class Veiculo:
    def __init__(self, nome, marca, ano, andando = False):
        self._nome = nome
        self._marca = marca
        self._ano = ano
        self.andando = andando

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor
        return self._nome

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._nome = valor
        return self._nome

    @property
    def ano(self):
        return self._ano

    @marca.setter
    def ano(self, valor):
        self._ano = valor
        return self._ano
    
    def andar(self):
        if not self.andando:
            print(f'{self.nome} está andando...')
            return
        if self.andando:
            print(f'{self.nome} já está andando...')
            return
        print(f'{self.nome} está andando...')
        self.andando = True
