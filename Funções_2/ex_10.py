'''
Crie uma função chamada "encontrar_substring" que
recebe uma string e uma substring como argumentos, e
retorna True se a substring estiver presente na string, e
False caso contrário
'''


def encontrar_substring(string: str, substring: str):
    for _ in string:
        if substring in string:
            return True
        return False


print(encontrar_substring('passei', 'assei'))
print(encontrar_substring('ola', 'pato'))
