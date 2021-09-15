# Classe
class Pessoa:
    # atributo de dado/atributo de instância
    def __init__(self, *filhos, nome=None, idade=28):  # def __init__(self, parâmetro)
        self.nome = nome  # "atributo.de_dado = parâmetro
        self.idade = idade
        self.filhos = list(filhos)  # atributo complexo

    # Método (atributo da classe)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(idade=35)
    tomas = Pessoa(idade=28)
    cleber = Pessoa(idade=40)
    luciano = Pessoa(renzo, tomas, cleber, nome='Luciano')
    # Chamando classe e método, precisa passar o objeto "p" (atributo da classe)
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    # Contudo, é possível chamar diretamente o próprio objeto "p", sem precisar passar o objeto novamente como parâmetro
    print(luciano.cumprimentar())
    print(luciano.nome)
    luciano.nome = 'Tomas'
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.idade)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)

