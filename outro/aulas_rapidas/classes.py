class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

controle_remoto = ControleRemoto('preto', '10cm', '4cm', '2cm')
controle_remoto.cor = 'verde'
print(controle_remoto)