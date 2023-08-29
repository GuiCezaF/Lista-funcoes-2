'''
Crie uma função chamada "contar_ocorrencias" que
recebe uma lista de elementos e um elemento específico
como argumentos, e retorna a quantidade de vezes que o
elemento aparece na lista
'''


def contar_ocorrencias(lista_elementos: list, elemento_especifico: any):
    contador = 0
    for elementos in lista_elementos:
        if elementos == elemento_especifico:
            contador += 1
    return contador


lista = [1, 5, 2, 1, 4, 1, 5, 70]
especifico = 1
retorno = contar_ocorrencias(lista, especifico)

print(retorno)
