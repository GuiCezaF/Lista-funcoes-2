'''
Crie uma função chamada "calcular_desconto" que
recebe o valor de um produto e uma porcentagem de
desconto como argumentos, e retorna o valor do produto
com o desconto aplicado
'''


def calcular_desconto(valor_produto: float, desconto: int):
    porcentagem = desconto / 100
    desconto_produto = valor_produto * porcentagem
    valor_final = valor_produto - desconto_produto
    return valor_final


produto = 100
desconto = 10
valor_produto_final = calcular_desconto(produto, desconto)
print(
    f'O produto que custa R${produto} com o desconto de {desconto}% sai por R${valor_produto_final}')
