from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('O saldo precisa ser numérico!')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('O valor precisa ser numérico!')
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhes(self):
        print(f'Agência: {self.agencia}')
        print(f'Conta: {self.numero}')
        print(f'Saldo: R$ {self.saldo}')


    