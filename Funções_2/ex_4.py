'''
Crie uma função chamada "calcular_media" que recebe
uma lista de números como argumento e retorna a média
aritmética dos elementos
'''


def calcular_media(lista_numeros):
    if not lista_numeros:
        return 'Lista vazia'  
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media



notas = [10, 7, 3, 9]
retorno = calcular_media(notas)
print(retorno)
