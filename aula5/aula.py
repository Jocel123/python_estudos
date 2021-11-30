class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

p1 = Pessoa('jeremias molvinho')
print(p1.nome.title())
p1.nome = 'Carlos'
print(p1.nome)
