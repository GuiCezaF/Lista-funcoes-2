'''
Crie uma função chamada "maior_numero" que recebe
uma lista de números como argumento e retorna o maior
número da lista
'''


def maior_numero(list_nums):
    lista_organizada = sorted(list_nums)
    index_lista = (len(lista_organizada) - 1)
    return lista_organizada[index_lista]


lista_nums = [10, 2, 3, 4, 5, 6, 7, 9]
maior_numero(lista_nums)
