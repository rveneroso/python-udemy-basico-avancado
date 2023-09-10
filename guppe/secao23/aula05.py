# def cabecalho(texto: str, alinhamento: bool = True) -> str:
#     if alinhamento:
#         return f"{texto.title()}\n{'-' * len(texto)}"
#     else:
#         return f" {texto.title()} ".center(50, '#')
#
#
# print(cabecalho('geek university'))
#
# print(cabecalho('geek university', alinhamento=False))
#
#
# print(cabecalho('geek university', alinhamento=True))
#

'''
Esse arquivo foi utilizado como exemplo na aula que falou sobre o mypy. Porém, se faz sentido utilizar o mypy
caso o código esteja escrito utilizando-se type hinting. Se o programa estiver escrito na forma tradicionalmente
utilizada em Python, o mypy não será capaz de identificar nenhuma anomalia no código mesmo que elas existam.
'''

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))


print(cabecalho('geek university', alinhamento=True))

cabecalho(texto='4', alinhamento=True)
