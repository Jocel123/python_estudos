class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, uf):
        self.enderecos.append(Endereco(cidade, uf))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f'{self.nome}')
            print(f'{endereco.cidade}-{endereco.uf}')

class Endereco:
    def __init__(self, cidade, uf):
        self.cidade = cidade
        self.uf = uf

cliente1 = Cliente('Pedro', 40)
cliente1.inserir_endereco('Caxias', 'MA')
cliente1.listar_enderecos()
print()

cliente2 = Cliente('Maria', 29)
cliente2.inserir_endereco('Belém', 'PA')
cliente2.listar_enderecos()
print()

cliente3 = Cliente('Gabriel', 47)
cliente3.inserir_endereco('Teresina', 'PI')
cliente3.listar_enderecos()
print()