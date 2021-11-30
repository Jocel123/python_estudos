class Teste:
    testar = 123
    def __init__(self):
        self.testar = 'Olá'


a1 = Teste()
a2 = Teste()
print(a1.testar)
print(a2.testar)
print(Teste.testar)