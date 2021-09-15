# Classe
class Pessoa:
    # atributo de dado
    def __init__(self, nome=None, idade=28):  # def __init__(self, parâmetro)
        self.nome = nome # "atributo.de_dado = parâmetro
        self.idade = idade

    # Método (atributo da classe)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    # Chamando classe e método, precisa passar o objeto "p" (atributo da classe)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    # Contudo, é possível chamar diretamente o próprio objeto "p", sem precisar passar o objeto novamente como parâmetro
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Tomas'
    print(p.nome)
    print(p.idade)
