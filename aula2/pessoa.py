from random import randint

class Pessoa:

    ano_atual = 2021

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod    
    def ano_nascimento(cls, nascimento):
        Idade = cls.ano_atual - nascimento
        return cls(Idade)

    @staticmethod
    def gera_id():
        rand = randint(1, 300)
        return rand
