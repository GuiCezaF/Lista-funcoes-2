'''
crie uma função chamada quadrado que recebe dois
parâmetros, um para a base e outro para a altura mostre
a borda de uma quadrado feito por asteriscos.
Por exemplo, para os valores 5 e 3 a saída de ser:
* * * * *
*       *
* * * * *
'''


def quadrado(base: int, altura: int):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print('* ' * base)
        else:
            print('* ' + '  ' * (base - 2) + '*')


base = int(input('Escreva o tamanho da base: '))
altura = int(input('Escreva o tamanho da altura: '))
quadrado(base, altura)
