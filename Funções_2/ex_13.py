
'''
rie uma função chamada quadrado que recebe dois
parâmetros, um para a base e outro para a altura mostre
um quadrado feito por asteriscos.
Por exemplo, para os valores 5 e 3 a saída de ser:
* * * * *
* * * * *
* * * * *
'''


def quadrado(base: int, altura: int):
    for i in range(1, altura + 1):
        print('* ' * base)


base = int(input('Escreva o tamanho da base: '))
altura = int(input('Escreva o tamanho da altura: '))
quadrado(base, altura)
