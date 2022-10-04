class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia de classe")

    def falar(self):
        print("auau")

c = Cachorro("dog","baranco", True)
c.falar()
del c