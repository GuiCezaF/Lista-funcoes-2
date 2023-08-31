'''
rie uma função chamada "calcular_raiz_quadrada" que
calcula a raiz quadrada de um número sem utilizar a
função de raiz quadrada embutida do Python (math.sqrt).
A função deve retornar o resultado com uma precisão de
duas casas decimais.
'''


def calcular_raiz_quadrada(num: float):
    raiz = num ** 0.5
    return raiz


numero = float(input('Digite um número: '))
print(f'A raiz quadrada de {numero} é {calcular_raiz_quadrada(numero): .2f}')
