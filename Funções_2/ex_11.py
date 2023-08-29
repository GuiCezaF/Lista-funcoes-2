'''
Crie uma função chamada "ordenar_lista" que recebe
uma lista de números como argumento e retorna uma
nova lista contendo os mesmos números, porém
ordenados de forma crescente.
'''

def ordenar_lista(lista_desordenada: list):
  return sorted(lista_desordenada)

lista = [60, 866, 19, 9, 986]
ordenado = ordenar_lista(lista)
print(f'A lista {lista} esta bagunçada, assim {ordenado} fica melhor')