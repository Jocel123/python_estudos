from corrente import ContaCorrent
from poupanca import ContaPoupanca

poup = ContaPoupanca(111, 222, 0)
poup.depositar(500)
poup.sacar(30)
poup.sacar(300)
poup.sacar(200)

print('\n#####################')

corrente = ContaCorrent(222, 444, 20)
corrente.depositar(20)
corrente.sacar(50)
corrente.sacar(30)