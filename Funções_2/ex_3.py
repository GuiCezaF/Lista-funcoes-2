'''
Crie uma função chamada "verificar_palindromo" que
recebe uma string como argumento e retorna True se a
string for um palíndromo (ou seja, pode ser lida da mesma
forma de trás para frente), e False caso contrário.
'''


def verificar_palindromo(string):
    string_invertida = string
    if string == string_invertida[::-1]:
        return True
    return False


verificar_palindromo('osso')
