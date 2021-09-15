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
    # atributo de classe "olhos" possui valor 2
    luciano.olhos = 1  # o objeto "luciano", através de uma atribuição dinâmica, possui "olhos" como um atributo de
    #                    instância que, apesar de possuir também "olhos" como atributo de classe, possui prioridade
    #                    sobre o mesmo
    del luciano.olhos  # ao deletar o atributo de instância "olhos" do objeto "luciano", ele passará a retornar o
    #                    valor de "olhos" referente ao atributo de classe (o que na atribuição dinâmica retornaria
    #                    um erro, se somente atribuído dinamicamente ou por instanciamento)
    Pessoa.olhos = 3  # se não fosse deletado o atributo de instância "olhos" do objeto "luciano", o valor a ser
    #                   retornado permaneceria sendo 1. Como foi deletado, todos os objetos do tipo Pessoa, agora,
    #                   retornam o valor 3 para o atributo "olhos", respectiva à classe
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
