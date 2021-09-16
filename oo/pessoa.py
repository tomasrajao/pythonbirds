# Classe
class Pessoa:
    olhos = 2  # atributo default/atributo de classe

    # atributo de dado/atributo de instância
    def __init__(self, *filhos, nome=None, idade=28):  # def __init__(self, parâmetro)
        self.nome = nome  # "atributo.de_dado = parâmetro
        self.idade = idade
        self.filhos = list(filhos)  # atributo complexo
        # os atributos de dado dessa classe são objetos do tipo Pessoa

    # Método (atributo da classe)
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    # métodos de classe
    @staticmethod  # método atrelado diretamente à classe
    def metodo_estatico():
        return 53

    @classmethod  # método de classe com acesso à classe que executa esse método
    def metodo_de_classe(cls):
        return f'{cls} {cls.olhos}'


class Homem(Pessoa):  # Herança: 'Homem' (classe Filha) herda de 'Pessoa' (classe Pai)
    def cumprimentar(self):  # sobrescrita de método. Executa apenas o método indicado na classe filho, mesmo que
        #                      exista na classe Pai
        cumprimentar_da_classe = Pessoa.cumprimentar(self)  # Classe.metodo(self): Maneira explícita de chamar o método
        #                                                     da classe Pai, porém não a ideal.
        cumprimentar_da_classe = super().cumprimentar()  # super().método(): Além de ser mais claro, o método especial
        #                                                  super() é a forma correta de chamar um método da classe Pai,
        #                                                  considerando que a classe Pai não precisa ser declarada
        #                                                  explicitamente
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3  # Sobrescrita de atributo: possui o mesmo nome que o atributo da classe Pai, sobrescrevendo o seu
    #            respectivo valor


if __name__ == '__main__':
    renzo = Homem(idade=35)
    tomas = Mutante(nome='Tomas', idade=28)
    cleber = Pessoa(idade=40)
    luciano = Pessoa(renzo, tomas, cleber, nome='Luciano')
    # Chamando classe e método, precisa passar o objeto "p" (atributo da classe)
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    # Contudo, é possível chamar diretamente o próprio objeto "p", sem precisar passar o objeto novamente como parâmetro
    print(luciano.cumprimentar())
    print(luciano.nome)
    luciano.nome = 'Tomas'
    luciano.nome = 'Luciano'
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.idade)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    # atributo de classe "olhos" possui valor 2
    luciano.olhos = 1  # o objeto "luciano", através de uma atribuição dinâmica, possui "olhos" como um atributo de
    #                    instância que, apesar de possuir também "olhos" como atributo de classe, possui prioridade
    #                    sobre o mesmo
    del luciano.olhos  # ao deletar o atributo de instância "olhos" do objeto "luciano", ele passará a retornar o
    #                    valor de "olhos" referente ao atributo de classe (o que na atribuição dinâmica retornaria
    #                    um erro, se somente atribuído dinamicamente ou por instanciamento)
    # Pessoa.olhos = 3  # se não fosse deletado o atributo de instância "olhos" do objeto "luciano", o valor a ser
    #                   retornado permaneceria sendo 1. Como foi deletado, todos os objetos do tipo Pessoa, agora,
    #                   retornam o valor 3 para o atributo "olhos", respectiva à classe
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)

    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.metodo_de_classe(), luciano.metodo_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(tomas, Pessoa))
    print(isinstance(tomas, Homem))
    print(tomas.olhos)
    print(renzo.cumprimentar())
    print(tomas.cumprimentar())

