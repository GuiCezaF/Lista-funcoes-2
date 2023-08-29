'''
Crie uma função chamada "verificar_anagrama" que
recebe duas strings como argumentos e retorna True se as
strings forem anagramas (ou seja, possuírem as mesmas
letras, independentemente da ordem), e False caso
contrário
'''


def verificar_anagrama(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    count_dic1 = {}
    count_dic2 = {}

    for car in str1:
        if car in count_dic1:
            count_dic1[car] += 1
        else:
            count_dic1[car] = 1

    for car in str2:
        if car in count_dic2:
            count_dic2[car] += 1
        else:
            count_dic2[car] = 1

    return count_dic1 == count_dic2


# Exemplos de uso
print(verificar_anagrama("ola", "alo"))  # Deve retornar True
print(verificar_anagrama("cansei", "de tudo"))    # Deve retornar False
