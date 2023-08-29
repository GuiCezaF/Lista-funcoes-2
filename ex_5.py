'''
Crie uma função chamada "calcular_potencia" que recebe
dois números como argumentos: a base e o expoente. A
função deve retornar a base elevada ao expoente.
'''
def calcular_potencia(base: int, expoente: int):
  return base ** expoente

base = int(input("digite um valor para a base: "))
expoente = int(input("digite um valor para o expoente: "))

retorno = calcular_potencia(base, expoente)
print(f'o resultado de {base} elevado a {expoente} potencia é igual á {retorno}')