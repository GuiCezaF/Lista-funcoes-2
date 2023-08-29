'''
Crie uma função chamada "contador_vogais" que recebe
uma string como argumento e retorna a quantidade de
vogais na string
'''


def contador_vogais(string):
    string_minuscula = string.lower()
    cont_vogais = 0
    vogais = ['a', 'e', 'i', 'o', 'u']

    for letras in string_minuscula:
        if letras in vogais:
            cont_vogais += 1

    return cont_vogais


palavra = input('Digite uma palavra para contar suas vogais: ')
num_vogais = contador_vogais(palavra)
print(f'A palavra {palavra} tem {num_vogais} vogais')
