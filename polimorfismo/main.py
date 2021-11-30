from abc import ABC, abstractmethod

class Carro(ABC):

    @abstractmethod
    def andar(self): pass

    @abstractmethod
    def acelerar(self): pass

class Fusca(Carro):
    def andar(self):
        print('Fusca está andando...')

    def acelerar(self):
        print('Fusca está acelerando...')

fusca = Fusca()
fusca.andar()
fusca.acelerar()