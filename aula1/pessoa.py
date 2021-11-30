from datetime import datetime

class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    #Método comer
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando!')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return
        print(f'{self.nome} parou de comer!')
        self.comendo = False

    #Métod0 falar
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar porque está comendo...')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando!')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if self.falando:
            print(f'{self.nome} não está falando...')
            return
            
        print(f'{self.nome} parou de falar...')
        self.falando = True

    def get_data_nascimento(self):
        return self.ano_atual - self.idade 
         
    