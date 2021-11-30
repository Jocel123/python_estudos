class Animal:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        nome_do_animal = self._nome = valor
        return nome_do_animal

    def comer(self):
        print(f'{self.nome} está comendo...')

class Cachorro(Animal):
    def latir(self):
        print(f'{self.nome} está latindo...')

class Lobo(Animal):
    def uivar(self):
        print(f'{self.nome} está uivando...')