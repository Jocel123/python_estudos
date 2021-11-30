from pessoa import Pessoa

p1 = Pessoa('Jocel', 33)
p1 = Pessoa.ano_nascimento(1988)
#print(p1.idade)
p1.ano_nascimento(1988)
print(p1.gera_id())